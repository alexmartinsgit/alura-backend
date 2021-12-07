from django.db import models

class videos(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    url = models.CharField(max_length=50)

