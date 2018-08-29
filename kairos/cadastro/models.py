from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Usuario(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    usuario = models.CharField(max_length = 30, unique = True)
    senha = models.CharField(max_length = 254)
    criacao = models.DateTimeField(auto_now = False, auto_now_add = True)
    ativo = models.BooleanField(default = False)

    def login(self, usuario, senha):
        try:
            usuario = Usuario.objects.get(usuario = usuario, senha = senha, ativo = True)
        except ObjectDoesNotExist:
            usuario = None

        return usuario


class Comprador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    cpf_cnpj = models.CharField(max_length = 14)


class Vendedor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    cpf_cnpj = models.CharField(max_length = 14)


class Contato(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    tipo = models.CharField(max_length = 30)
    pais = models.IntegerField()
    codigo_regiao = models.IntegerField()
    numero = models.IntegerField()


class EnderecoEntrega(models.Model):
    cep = models.IntegerField()
    logradouro = models.CharField(max_length = 20)
    endereco = models.CharField(max_length = 255)
    numero = models.CharField(max_length = 10)
    complemento = models.CharField(max_length = 50)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class EnderecoCobranca(models.Model):
    cep = models.IntegerField()
    logradouro = models.CharField(max_length = 20)
    endereco = models.CharField(max_length = 255)
    numero = models.CharField(max_length = 10)
    complemento = models.CharField(max_length = 50)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)