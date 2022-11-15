from django.urls import path
from.import views
from django.urls import include


urlpatterns = [
    path('', views.home, name= 'home'),
    path('about', views.about, name='about'),
    path('dietas', views.dietas, name='dietas'),
    path('rutinas', views.rutinas, name='rutinas'),

    #dietas:
    path('dietas/d1', views.d1, name= 'd1'),
    path('dietas/d2', views.d2, name= 'd2'),
    path('dietas/d3', views.d3, name= 'd3'),

    #rutinas:
    path('rutinas/r1', views.r1, name= 'r1'),
    path('rutinas/r2', views.r2, name= 'r2'),
    path('rutinas/r3', views.r3, name= 'r3'),

    #formularios;
    path('form', views.form, name='form'),
    path('registro/', views.registro, name='registro'),
    path('register', views.register, name='register'),
    #path('login', views.login, name='login'), no necesaria
    
    path('revision', views.revision, name='revision'),
    
    path('contacto', views.contacto, name='contacto'),
    #path('contacto1', views.contacto1, name='contacto1'), #pruebas


    #path('accounts/', include('django.contrib.auth.urls')),
]