from django.views.generic import FormView

from .forms import LoginForm

class IndexView(FormView):
    template_name = 'login/index.html'
    form_class = LoginForm
    success_url = '/'