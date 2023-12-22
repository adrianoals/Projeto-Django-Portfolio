from django.db import models

class ProjetoWebAPI(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(max_length=200)
    imagem = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.nome

