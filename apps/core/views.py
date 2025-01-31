from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user  # pega o usuario do sistema
    return render(request, 'core/index.html', data)
