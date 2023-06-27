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

# 개발중
def get_file_from_s3(bucket_name, object_name):
    s3_client = boto3.client('s3', 
                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, 
                             region_name=settings.AWS_S3_REGION_NAME)
    response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
    # 이 부분은 BytesIO 객체를 반환합니다.
    # 이 객체는 파일과 같이 동작하므로, 파일을 요구하는 대부분의 함수/메서드에서 사용할 수 있습니다.
    return BytesIO(response['Body'].read())

