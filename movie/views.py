from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Dieta, Rutina
from .forms import UsuarioForm, ContactoForm, ImcForm, CustomUserCreationForm, DietaForm, RutinaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from .static import recomendador

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
    #data = recomendador
    return render(request, 'dietas.html', {'dietas': dietas })#, {'data': data})

def rutinas(request):
    rutinas = Rutina.objects.all()
    #data = recomendador
    return render(request, 'rutinas.html', {'rutinas': rutinas})#, {'data': data})


#dietas:
def d1(request):
    #formulario = DietaForm(request.POST or None)
    #messages.info(request, "Pronto podrás revisar todos tus elementos guardados.")
    return render(request, 'dietas/d1.html')#, {'formulario': formulario})

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
        messages.success(request, "Sus datos se completaron y registraron con éxito.")  # prueba de funcionalidad
        return redirect('home')
    
    
    return render(request, 'formulario/register.html', {'formulario': formulario})


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Sus Datos fueron registrados con exito," "Bienvenido a Living")
            #redrigir
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#def login(request):
#    return render(request, 'formulario/login.html')

#def contacto(request):
#    data = {
#        "form": ContactoForm()
#    }
#    if request.method == 'POST':
#        formulario = ContactoForm(data=request.POST)
#        if formulario.is_valid():
 #           formulario.save()
 #           data["mensaje"] = "contacto guardado"
 #       else:
 #           data["form"] = formulario
 #   return render(request, 'formulario/contacto.html', data)

def contacto(request):
    formulario = ContactoForm(request.POST or None)
    if formulario.is_valid():
            formulario.save()
            messages.success(request, "Su comentario será revisado por nuestro grupo de trabajo")
            return redirect('contacto')
    return render(request, 'formulario/contacto.html', {'formulario': formulario})

def revision(request):
    return render(request, 'formulario/revision.html')
