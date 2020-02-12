from django.shortcuts import render
from django.views.generic import CreateView
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *arqs, **kwargs):
        form = self.get.form()
        form.instance.pertence_id = self.kwargs('funcionario.id')

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
