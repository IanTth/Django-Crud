from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length = 10)
    valor = models.CharField(max_length = 10)
    descrição = models.CharField(max_length = 50)
    quantidade = models.CharField(max_length = 50)
   
