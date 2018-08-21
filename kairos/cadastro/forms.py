from django import forms

from .models import Usuario

class CadastrarUsuario(forms.ModelForm):

    nome = forms.CharField(label = 'Nome')
    sobrenome = forms.CharField(label = 'Sobrenome')
    email = forms.CharField(label = 'E-mail')
    confirma_email = forms.CharField(label = 'Confirmar E-mail')
    login = forms.CharField(label = 'Login')
    senha = forms.CharField(widget=forms.PasswordInput(), label = 'Senha')
    confirma_senha = forms.CharField(widget=forms.PasswordInput(), label = 'Confirmar senha')

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'confirma_email', 'login', 'senha', 'confirma_senha']

    def clean(self):
        cleaned_data = super().clean()

        senha = cleaned_data.get('senha')
        confirma_senha = cleaned_data.get('confirma_senha')

        email = cleaned_data.get('email')
        confirma_email = cleaned_data['confirma_email']

        if senha != confirma_senha:
            raise forms.ValidationError(
                'Senha não confere! Digite a mesma senha nos campos Senha e Confirmar Senha.'
            )

        if email and confirma_email:
            if email != confirma_email:
                raise forms.ValidationError(
                    'E-Mail não confere! Digite o mesmo e-mail nos campos E-mail e Confirma E-mail'
                )

        return cleaned_data