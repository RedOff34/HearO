from django.shortcuts import render
import os
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Location
from django.contrib.auth.decorators import login_required
from Main.models import History
from django.utils import timezone

@login_required
@csrf_exempt
def show_location(request):
    return render(request, 'app/location.html')

@login_required  
@csrf_exempt
def save_location(request):
    if request.method == 'POST':
        address = request.POST['address']

        loc, created = Location.objects.update_or_create(
            user_id=request.user, 
            defaults={'location': address,'timestamp': timezone.now()}
        )

        return JsonResponse({"status": "success", "message": "Location saved successfully"})


@login_required
@csrf_exempt
def get_user_danger(request):
    user = request.user

    # 최신 위치를 가져옵니다.
    latest_location = Location.objects.filter(user=user).order_by('-timestamp').first()

    if latest_location is not None:
        unicode_location = latest_location.location
        decoded_location = unicode_location.encode('utf-8').decode('unicode_escape')
        
        unicode_address = user.address
        decoded_address = unicode_address.encode('utf-8').decode('unicode_escape')
        
        danger_info = {
            'user_name': user.name,
            'user_address':user.address,
            'location': latest_location.location,
            'timestamp': latest_location.timestamp.strftime("%Y-%m-%d %H:%M"),
            'danger_type' : '폭행',
            'file' : 'file'
        }
        history = History(user_id=user.user_id, user_name=user.name, user_address=user.address, location=latest_location.location, date=danger_info['timestamp'], danger_type=danger_info['danger_type'], file=danger_info['file'])
        history.save()
    else:
        danger_info = {
            'user_id': user.user_id,
            'message': 'No location data available for this user.',
        }
    
    return JsonResponse(danger_info)
