from ctypes.wintypes import HENHMETAFILE
from turtle import color
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

"""
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Juan Esteban Pavas González'})
def about(request):
    return render(request, 'about.html')
"""
def home(request):
    #return render(request, 'home.html', {'name': 'Juan Esteban Pavas González'})
    #return HttpResponse("<h1>Bienevnido a Living</h1>")
    return render (request, 'home.html')
def about(request):
    return render(request, 'about.html')
def dietas(request):
    return render(request, 'dietas.html')
def rutinas(request):
    return render(request, 'rutinas.html')

#dietas:
def d1(request):
    return render(request, 'dietas/d1.html')
def d2(request):
    return render(request, 'dietas/d2.html')
def d3(request):
    return render(request, 'dietas/d3.html')
#rutinas:
def r1(request):
    return render(request, 'rutinas/r1.html')
def r2(request):
    return render(request, 'rutinas/r2.html')
def r3(request):
    return render(request, 'rutinas/r3.html')

#formulario:
def form(request):
    return render(request, 'formulario/form.html')