from turtle import color
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Juan Esteban Pavas González'})
def about(request):
    return render(request, 'about.html')