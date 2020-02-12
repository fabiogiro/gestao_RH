from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario, User
from django.urls import reverse_lazy


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ('nome', 'departamentos')


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario_list')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ('nome', 'departamentos')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        listnome = funcionario.nome.split(' ')
        username = listnome[0] + listnome[len(listnome) - 1]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)
