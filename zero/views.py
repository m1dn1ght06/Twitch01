from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return HttpResponse('Hello World')

def Shop(request):
    return HttpResponse('Hello World')

def contactus(request):
    return HttpResponse('Hello World')