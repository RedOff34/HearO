# Main/models.py

from django.db import models
from SignIn.models import User


# Create your models here.



class Post(models.Model):
    post_id = models.AutoField(primary_key=True) # 게시물 번호 정수로 변경한 이유는 순서별로 정렬하기 위해
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 글 작성자 id 
    title = models.CharField(max_length=20) # 글 제목
    content = models.CharField(max_length=300) # 글의 내용 
    date = models.DateTimeField(auto_now_add = True) # 글쓴 시간 년 월 일 시간 까지
    file = models.FileField(upload_to='', null=True) # 파일 media 에 저장
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True) # 댓글 번호
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 작성자 id
    content = models.TextField(max_length=100) # 댓글 내용 최대 100
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 댓글이 달린 게시글 id 
    date = models.DateTimeField(auto_now_add = True)  # 댓글 쓴 시간 년 월 일 시간 까지
    
class History(models.Model):
    hist_id = models.AutoField(primary_key=True) # 신고 번호
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 신고한 유저 id
    user_name = models.CharField(max_length =20)
    user_address = models.CharField(max_length=20)
    date = models.DateTimeField() # 신고 시간 년 월 일 시간 까지
    danger_type = models.CharField(max_length=200)
    location = models.CharField(max_length=50) # 신고 당시 위치
    file = models.CharField(max_length=500) # 파일 이름 
    

class Audio(models.Model):
    audio = models.FileField(upload_to='sound/')
    
class Setting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 글 작성자 id 
    sensitivity = models.IntegerField()
    count = models.IntegerField()
