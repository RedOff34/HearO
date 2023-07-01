from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
import boto3
from io import BytesIO
from django.conf import settings
def logout_required(function=None, redirect_url='/Main'):
    """
    Decorator for views that checks that the user is logged out, redirecting
    to the specified page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

# 파일 다운로드
def get_file_from_s3(object_name, local_dir='media/sound'): # local_dir 저장할 파일경로
    s3_client = boto3.client('s3', 
                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, 
                             region_name=settings.AWS_S3_REGION_NAME)
    response = s3_client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_name)
    object_name1 = object_name.split('/')[-1] 
    local_file_path = os.path.join(local_dir, object_name1)
    s3_client.download_file(settings.AWS_STORAGE_BUCKET_NAME, object_name, local_file_path)
    return local_file_path

#데이터를 BytesIO형식으로 받아오기
def load_file_from_s3(s3_key):# s3_ket는 파일 이름
    s3 = boto3.client('s3',
                       aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, 
                             region_name=settings.AWS_S3_REGION_NAME)
    obj = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=s3_key)
    data = BytesIO(obj['Body'].read())
    return data

#BytesIO형식을 소리파일로 변환
def load_audio_from_s3(s3_key):
    data = load_file_from_s3(s3_key)
    data.seek(0)  # Make sure to seek to the start of your BytesIO object
    audio = AudioSegment.from_file(data, format="wav")
    return audio

