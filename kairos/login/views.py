from django.views.generic import FormView, UpdateView

from .forms import LoginForm, EsqueciSenhaForm
from cadastro.models import Usuario

class IndexView(FormView):
    template_name = 'login/index.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        usuario = form.cleaned_data.get('usuario')
        senha = form.cleaned_data.get('senha')
        usuario_valido = Usuario.login(Usuario, usuario, senha)

        if usuario_valido is not None:
            self.success_url = '/'
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Usuário ou senha inválido!')
        return super().form_invalid(form)

class EsqueciSenhaView(FormView):
    template_name = 'login/esqueci_senha.html'
    form_class = EsqueciSenhaForm