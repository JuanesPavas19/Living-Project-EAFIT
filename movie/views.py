from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Dieta, Rutina
from .forms import UsuarioForm, ContactoForm, ImcForm
from django.contrib import messages

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
    dietas = Dieta.objects.all()
    return render(request, 'dietas.html', {'dietas': dietas })

def rutinas(request):
    rutinas = Rutina.objects.all()
    return render(request, 'rutinas.html', {'rutinas': rutinas})

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
    formulario = ImcForm(request.POST or None)
    ##imc = ImcForm(request=imcs)
    #if imc < 18.5:
    #    messages.success(request, "Rango de Peso Insuficiente")
    #    return redirect('form')
    #elif imc >= 18.5 or imc < 25.0 :
    #    messages.success(request, "Rango de Peso Normal o Saludable")
     #   return redirect('form')
    #elif imc >= 25.0 or imc < 30.0 :
    #    messages.success(request, "Rango de Sobrepeso")
    #    return redirect('form')
    #elif imc > 29.9:
    #    messages.success(request, "Rango de Obesidad")
    #    return redirect('form')  
    return render(request, 'formulario/form.html', {'formulario': formulario})#, {'imc': imc})

def register(request):
    formulario = UsuarioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Datos Registrados","tus Datos fueron registrados con exito", "error")  # prueba de funcionalidad
        return redirect('home')
    return render(request, 'formulario/register.html', {'formulario': formulario})

def login(request):
    return render(request, 'formulario/login.html')

def contacto(request):
    data = {
        "form": ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'formulario/contacto.html', data)

def contacto1(request):
    formulario = ContactoForm(request.POST or None)
    if formulario.is_valid():
            formulario.save()
            messages.success(request, "Comentario Enviado")
            return redirect('contacto1')
    return render(request, 'formulario/contacto1.html', {'formulario': formulario})
