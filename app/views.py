from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/index.html', {})

def home_flights(request):
    return render(request, 'app/index.html', {})

def home_hotel(request):
    return render(request, 'app/index.html', {})

def contact(request):
    return render(request, 'app/contact.html', {})

def dev(request):
    # return HttpResponse("request.path: {}, \n request.get_host(): {},\n request.get_full_path(): {}, request.is_secure(): {}".format(request.path, request.get_host(), request.get_full_path(), request.is_secure()))
    return HttpResponse(request.META)