from django.shortcuts import HttpResponse, redirect
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.


def hellow_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')


def now_date(request):
    current_date = timezone.now().date()
    return HttpResponse(current_date)