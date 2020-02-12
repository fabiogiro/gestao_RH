from django.urls import reverse
from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome

    def get_absulute_url(self):
        return reverse('home')
