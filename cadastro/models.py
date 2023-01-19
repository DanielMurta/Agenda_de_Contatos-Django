from django.db import models

# Criando os campos no banco de dados
class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    email = models.EmailField()
    numero_telefone = models.IntegerField()
