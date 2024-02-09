from django.db import models
from datetime import datetime

class ProjetoWebAPI(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(max_length=300)
    imagem = models.CharField(max_length=150, null=False, blank=False)
    data_criacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome

class ProjetoAutomacao(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(max_length=300)
    imagem = models.CharField(max_length=150, null=False, blank=False)
    data_criacao = models.DateTimeField(default=datetime.now, blank=False)
    

    def __str__(self):
        return self.nome

class ProjetoMobile(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(max_length=300)
    imagem = models.CharField(max_length=150, null=False, blank=False)
    data_criacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome

