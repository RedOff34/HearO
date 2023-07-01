from django import forms

from .models import Post, Comment, Audio
class PostModelForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width:100%; border:1px solid #ced4da', 'rows': '1', 'placeholder': '20자 이내', 'maxlength': '100', 'required': True}),
        label='제목'
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width:100%; border:1px solid #ced4da', 'rows': '10', 'placeholder': '300자 이내', 'maxlength': '300'}),
        label='내용'
    )
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'upload-file', 'id': 'input-file'}),
        label='파일 첨부',
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': False}),
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
        fields = ['title', 'content']
        

class CommentModelForm(forms.ModelForm): # 댓글 작성
    
    class Meta:
        model = Comment
        fields = ['content']
        
class AudioForm(forms.Form):
    audio_file = forms.FileField()