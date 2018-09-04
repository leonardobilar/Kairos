from django.views.generic import FormView
from django.shortcuts import redirect

from .forms import LoginForm, EsqueciSenhaForm
from cadastro.models import Usuario

class LoginView(FormView):
    template_name = 'login/index.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        usuario = form.cleaned_data.get('usuario')
        senha = form.cleaned_data.get('senha')
        usuario_valido = Usuario.login(Usuario, usuario, senha)

        if usuario_valido is not None:
            self.success_url = '/'
            self.start_session(usuario_valido)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Usuário ou senha inválido!')
        return super().form_invalid(form)

    def start_session(self, usuario):
        self.request.session['id'] = usuario.pk
        self.request.session['nome'] = usuario.nome


#Finaliza a sessão identificada
def logout(request):
    del request.session['id']
    del request.session['nome']
    return redirect('/')


class EsqueciSenhaView(FormView):
    template_name = 'login/esqueci_senha.html'
    form_class = EsqueciSenhaForm