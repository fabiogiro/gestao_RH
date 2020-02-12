from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcioanrio = self.request.user.funcionario
        funcioanrio.empresa = obj
        funcioanrio.save()
        return HttpResponse('OK')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
