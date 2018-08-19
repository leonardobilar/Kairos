from django import forms
from django.contrib.auth.hashers import make_password

from .models import Usuario

class CadastrarUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'login', 'senha',]
        widgets = {
            'senha': forms.PasswordInput(),
        }