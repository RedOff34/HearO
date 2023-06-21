from django import forms

from .models import Post, Comment, Audio
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        labels = {
            'file': '파일 첨부',
        }
        help_texts = {
            'file': '선택적으로 파일을 첨부할 수 있습니다.',
        }
        error_messages = {
            'file': {
                'max_length': "파일 이름이 너무 깁니다. 다른 이름으로 저장하세요.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False
        
class PostUpdateForm(forms.ModelForm): # 글 수정

    class Meta:
        model = Post
        fields = ['title', 'content', 'file']
        

class CommentModelForm(forms.ModelForm): # 댓글 작성
    
    class Meta:
        model = Comment
        fields = ['content']
        
class AudioForm(forms.Form):
    audio_file = forms.FileField()