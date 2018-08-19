from django.contrib.auth.hashers import make_password
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    login = models.CharField(max_length = 30, unique = True)
    senha = models.CharField(max_length = 255)
    criacao = models.DateTimeField(auto_now = False, auto_now_add = True)
    ativo = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        #criptografia
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)