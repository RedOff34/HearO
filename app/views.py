from django.shortcuts import render
import os
import shutil
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from .models import Location, danger
from SignIn.models import User 
from django.contrib.auth.decorators import login_required
from Main.models import History, Setting
from django.utils import timezone
from django.conf import settings
import boto3
import os
import requests, json 
import googlemaps
import time


@login_required
@csrf_exempt
def get_setting(request: HttpResponse):
    user = request.user
    setting = Setting.objects.get(user=user)
    user_setting = {
        'user': setting.user.user_id,
        'sensitivity' : setting.sensitivity,
        'count': setting.count, 
    }
    return JsonResponse(user_setting)
    
    


@login_required
@csrf_exempt
def get_latest_history(request: HttpResponse):
    user = request.user
    latest_history = History.objects.filter(user=user).order_by('-date').first()
    userhistory = {
        'user_id':latest_history.user.user_id,
        'user_name':latest_history.user_name, 
        'user_address':latest_history.user_address,
        'location':latest_history.location, 
        'date':latest_history.date, 
        'danger_type':latest_history.danger_type, 
        'file':latest_history.file.name,
    }
    return JsonResponse(userhistory)

@login_required
@csrf_exempt
def get_latest_danger(request: HttpResponse):
    user = request.user
    latest_danger = danger.objects.filter(user=user).order_by('-timestamp').first()
    userdanger = {
        'user_id':latest_danger.user.user_id,
        'user_name':latest_danger.user.name, 
        'danger_type':latest_danger.danger_type,
        'sound_file':latest_danger.soundfile,
        'prob':latest_danger.prob, 
        'time':latest_danger.timestamp,
    }
    return JsonResponse(userdanger)

# def current_location():
#     key = 'AIzaSyBWyrdzNJz964bPNMJ6Lfla_w-mcch-Tmw'
#     url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={key}'
#     data = {
#     'considerIp': True, # 현 IP로 데이터 추출
#     }
#     result = requests.post(url, data)    
#     print(result.text)
#     location = json.loads(result.text)
#     lat = location["location"]["lat"] # 현재 위치의 위도 추출
#     lng = location["location"]["lng"] # 현재 위치의 경도 추출
#     gmaps = googlemaps.Client(key)
#     address = gmaps.reverse_geocode((lat, lng),language='ko')
#     return address[0]['formatted_address']

@login_required
def popup1(request):
    return render(request, 'main/popup1.html')
 
@login_required
def popup2(request):
    return render(request, 'main/popup2.html')

@login_required
@csrf_exempt
def task_emergency_file(request: HttpResponse):
    user = request.user
    user_id = user.user_id
    folder_path = './media/sound_history/'
    folder_path = os.path.join(folder_path, user_id+ '/')
    files = os.listdir(folder_path)
    files.sort(reverse=True)
    save_danger_from_file(request)
    return HttpResponse("task complete")

@login_required
@csrf_exempt
def send_message(request:HttpResponse):
    user = request.user
    user_id = user.user_id

@login_required
@csrf_exempt
def upload_s3(request: HttpResponse):
    user = request.user
    user_id = user.user_id
    folder_path = './media/sound_history/'
    folder_path = os.path.join(folder_path, user_id + '/')
    files = os.listdir(folder_path)
    files.sort(reverse=True)
    print(files)
    file_path = os.path.join(folder_path, files[0])
    session = boto3.session.Session()
    s3_client = session.client(
            service_name='s3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
            )
    response = s3_client.upload_file(file_path,'hearo-sound', os.path.join('sound/',files[0]))
    return HttpResponse("s3 upload complete")

@login_required
@csrf_exempt
def remove_file(request: HttpResponse):
    time.sleep(3)
    user = request.user
    user_id = user.user_id
    folder_path = './media/sound_history/'
    folder_path = os.path.join(folder_path, user_id +'/')
    files = os.listdir(folder_path)
    files.sort(reverse=True)
    os.remove(os.path.join(folder_path, files[0]))
    return HttpResponse("task complete")

@login_required
@csrf_exempt
def get_folder_contents(request: HttpResponse):
    user = request.user
    user_id = user.user_id
    folder_path = './media/sound_history/'
    folder_path = os.path.join(folder_path, user_id)  # 조회할 폴더 경로 설정
    print(folder_path)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    # 폴더 내 파일 목록 조회
    file_list = os.listdir(folder_path)
    
    # 파일 목록을 JSON 형식으로 변환하여 응답
    return JsonResponse({'files': file_list})
 
#from hearo.utils import download_from_s3
@login_required
@csrf_exempt
def show_location(request):
    return render(request, 'app/location.html')  

@login_required
@csrf_exempt
def save_location(request):
    if request.method == 'POST':
        address = request.POST['address']
        # '대한민국' 제거
        address = ' '.join(address.split(' ')[1:])

        loc, created = Location.objects.update_or_create(
            user_id=request.user, 
            defaults={'location': address,'timestamp': timezone.now()}
        )

        return JsonResponse({"location":address, "status": "success", "message": "Location saved successfully"})

@login_required
@csrf_exempt
def get_user_danger(request:HttpResponse):
    user = request.user
    latest_location = Location.objects.filter(user=user).order_by('-timestamp').first()
    latest_danger = danger.objects.filter(user=user).order_by('-timestamp').first()
    if latest_danger is not None:
        danger_info = {
            'user_name': user.name,
            'user_address':user.address,
            'location': latest_location.location,
            'timestamp': latest_danger.timestamp.strftime("%Y-%m-%d %H:%M"),
            'danger_type' : latest_danger.danger_type,
            'file' : latest_danger.soundfile,
        }
        history = History(user_id=user.user_id, user_name=user.name, user_address=user.address, location=danger_info['location'], date=danger_info['timestamp'], danger_type=danger_info['danger_type'], file=danger_info['file'])
        history.save()
    else:
        danger_info = {
            'user_id': user.user_id,
            'message': 'No location data available for this user.',
        }
    return JsonResponse(danger_info)


def my_view(request):
    get_file_from_s3('cat.jpg')
    return HttpResponse("File downloaded successfully.")




def save_danger_from_file(request:HttpResponse):
    user = request.user
    user_id = user.user_id
    user_name = user.name
    folder_path = './media/sound_history/'
    folder_path = os.path.join(folder_path, user_id)
    files = os.listdir(folder_path)
    files.sort(reverse=True)
    # 분해, 분석 및 값 할당
    parts = files[0].split("_")
    user_id = parts[0]
    danger_num_to_str = {0:'강제추행(성범죄)', 1:'강도범죄', 2:'절도범죄',3:'폭력범죄',
                         4:'화재',5:'갇힘',6:'응급의료',7:'전기사고',8:'가스사고',
                         9:'낙상',10:'붕괴사고',11:'도움요청'}
    danger_type = danger_num_to_str[int(parts[-2])]
    soundfile = "https://hearo-sound.s3.ap-northeast-2.amazonaws.com/sound/" + files[0]
    prob = parts[-1].split(".")[0]
    # User instance 가져오기 (예를 들어, user_id가 실제 사용자의 username에 해당한다고 가정)
    user = User.objects.get(name=user_name)
    
    # 새로운 danger 인스턴스 생성 및 저장
    danger_instance = danger(user=user, danger_type=danger_type, soundfile=soundfile, prob=prob, timestamp= timezone.now())
    danger_instance.save()
    return JsonResponse({"status": "success", "message": "danger instance saved successfully"})