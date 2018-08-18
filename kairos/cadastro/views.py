from django.shortcuts import render
from django.views import generic

from .models import Usuario

class IndexView(generic.ListView):
    template_name = 'cadastro/index.html'
    context_object_name = 'usuario'

    def get_queryset(self):
        return Usuario.objects