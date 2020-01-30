from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do Departamento", blank=False, null=False)

    def __str__(self):
        return self.nome
