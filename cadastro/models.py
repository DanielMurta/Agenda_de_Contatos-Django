from django.db import models

class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    email = models.EmailField()
    numero_telefone = models.IntegerField()
