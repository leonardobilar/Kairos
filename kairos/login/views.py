from django.views.generic import FormView

from .forms import LoginForm
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
            return super().form_invalid(form)

    def form_invalid(self, form):
        raise