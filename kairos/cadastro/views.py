from django.views.generic import CreateView

from .models import Usuario
from .forms import CadastrarUsuario

class IndexView(CreateView):
    template_name = 'cadastro/index.html'
    model = Usuario
    form_class = CadastrarUsuario
    success_url = '/cadastro'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid()