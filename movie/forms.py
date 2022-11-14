from django import forms
from .models import Usuario, Contacto, Imc

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