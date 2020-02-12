from .models import RegistroHoraExtra
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
# para pegar somente os funcionarios da empresa logada
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
'''
    fields = ['motivo', 'funcionario', 'horas']
'''

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
# para pegar somente os funcionarios da empresa logada
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo,self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

'''
    fields = ['motivo', 'funcionario', 'horas']

    def form_valid(self, form):
        horaextra = form.save(commit=False)
        horaextra.empresa = self.request.user.funcionario.empresa
        horaextra.save()
        return super(HoraExtraNovo, self).form_valid(form)
'''