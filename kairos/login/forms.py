from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}), label = 'Usuário')
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_field'}), label='Senha')

class EsqueciSenhaForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs = {'class': 'input_field'}), label = 'E-mail')