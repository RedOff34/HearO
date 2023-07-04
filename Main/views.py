# Main/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from .forms import PostModelForm, PostUpdateForm, CommentModelForm
from .models import Post, Comment, Audio, Setting
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from Main.models import History
from django.core import serializers
from django.core.files import File
from pydub import AudioSegment
from django.views.generic import View
import os

# Create your views here.
@login_required
def Index(request):
    return render(request, 'main/main.html')
def Info(request):
    return render(request, 'main/info.html')
def MyPage(request): 
    return render(request, 'main/MyPage.html')

def PostMove(request):
    posts = Post.objects.all()  # 모든 게시물 가져오기
    return render(request, 'main/Post.html', {'posts': posts})

@login_required
def Settings(request):
    if request.method == "POST":
        sensitivity = request.POST.get('sensitivity')
        count = request.POST.get('count')

        Setting.objects.update_or_create(user=request.user, defaults={'sensitivity': sensitivity, 'count': count})

        return redirect('/Main/')
    else:
        settings = Setting.objects.filter(user=request.user).first()
        return render(request, 'main/Settings.html', {'settings': settings})

def PostNew(request):
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)  # 파일 데이터(request.FILES)를 전달
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/Main/Post/', pk=post.pk)
    else:
        form = PostModelForm()
    return render(request, 'main/PostEdit.html', {'form': form})


def PostView(request, pk):
    post = get_object_or_404(Post, post_id=pk) # 게시글 내용
    comment = Comment.objects.filter(post = post) # 댓글 내용
    if post.file:  # 파일 필드가 비어있지 않은 경우에만 파일 URL을 설정 , 게시글 보이는 부분
        file_url = post.file.url
    else:
        file_url = None

    if request.method == "POST": # 댓글 작성 부분
        form = CommentModelForm(request.POST)  
        if form.is_valid():
            comment1 = form.save(commit=False)
            comment1.user = request.user
            comment1.post = post
            comment1.save()
            
            return redirect('/Main/Post/{post_id}/'.format(post_id=post.post_id))
    else:
        form = CommentModelForm()
    return render(request, 'main/PostView.html', {'post': post, 'file_url': file_url, 'comment':comment, 'form':form})

    
def PostUpdate(request, pk):
    blog = Post.objects.get(post_id=pk)

    # 글을 쓴 사람만 수정할 수 있도록 권한을 체크합니다.
    if blog.user != request.user:
        messages.error(request, "글을 수정할 수 있는 권한이 없습니다.")
        return redirect('/Main/Post/{post_id}/'.format(post_id=pk))

    if request.method == "POST":
        form = PostUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.content = form.cleaned_data['content']
            blog.date = timezone.now()
            blog.save()

            return redirect(f'/Main/Post/{blog.post_id}/', pk=blog.pk)
    else:
        form = PostUpdateForm(instance=blog)
    return render(request, 'main/PostUpdate.html', {'form': form})

def PostDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        if request.method == "POST":
            post.delete()
            messages.success(request, "글을 삭제했습니다.")
            return redirect('/Main/Post/')
    else:
        messages.error(request, "글을 삭제할 수 있는 권한이 없습니다.")
    return redirect('/Main/Post/{post_id}/'.format(post_id=pk))

def DeleteComment(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id)
    if comment.user == request.user:
        if request.method == "POST":
            comment.delete()
            messages.success(request, "댓글을 삭제했습니다.")
        else:
            messages.error(request, "잘못된 요청입니다.")
    else:
        messages.error(request, "댓글을 삭제할 수 있는 권한이 없습니다.")
    
    return redirect('/Main/Post/{post_id}/'.format(post_id=comment.post.post_id))


def save_audio(request):
    if request.method == 'POST':
        
        audio_file = request.FILES.get('audio_file')

        if audio_file:
            user_id = request.user.user_id  # 현재 로그인된 사용자의 ID를 가져옵니다.
            folder_name = f"{user_id}"
            folder_path = './media/sound_history/' + folder_name
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            # 파일 이름에 사용자 ID를 추가합니다.
            file_name = f"{user_id}_{audio_file.name}"
            audio = AudioSegment.from_file(audio_file, format="webm")
            new_path = './AI/sound/' + file_name
            audio.export(new_path, format="wav")
            return JsonResponse({'message': 'File saved successfully'})
        else:
            return JsonResponse({'message': 'File save failed'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    
    
 
@login_required
def get_user_history(request):
    user = request.user

    # 로그인된 사용자의 History 객체들만 가져옵니다.
    user_history = History.objects.filter(user=user)

    # JSON 응답을 위해 QuerySet을 직렬화합니다.
    user_history_json = serializers.serialize('json', user_history)

    return HttpResponse(user_history_json, content_type='application/json')


def map_view(request):
    return render(request, 'main/map.html')


def popup1(request):
    user = request.user
    # 최신 History를 가져옵니다.
    latest_history = History.objects.filter(user=user).order_by('-date').first()
    if latest_history is not None:
        danger_info = {
            'user_name': user.name,
            'user_address': user.address,
            'location': latest_history.location,
            'timestamp': latest_history.date.strftime("%Y-%m-%d %H:%M"),
            'danger_type' : latest_history.danger_type,
            'file' : latest_history.file.url if latest_history.file else None,
        }
    else:
        danger_info = {
            'user_id': user.user_id,
            'message': '정보가 존재하지 않습니다.',
        }

    # danger_info를 context에 추가합니다.
    context = {
        'danger_info': danger_info,
    }

    return render(request, 'main/popup1.html', context)


def popup2(request):
    return render(request, 'main/popup2.html')

@login_required
def HistoryView(request):
    his = History.objects.filter(user=request.user)
    return render(request, 'main/UserHistory.html', {'his':his})

class ServiceWorkerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'firebase-messaging-sw.js', content_type="application/x-javascript")
