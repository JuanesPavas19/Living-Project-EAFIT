from django import forms
from .models import Usuario, Contacto, Imc, r_rutina, r_dieta
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= '__all__'

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje","avisos"]
        fields = '__all__'

class ImcForm(forms.ModelForm):
    class Meta:
        model = Imc
        fields = '__all__'
        #imcs = Imc._get_imc()

class DietaForm(forms.ModelForm):
    class Meta:
        model = r_dieta
        fields = '__all__'

class RutinaForm(forms.ModelForm):
    class Meta:
        model = r_rutina
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass