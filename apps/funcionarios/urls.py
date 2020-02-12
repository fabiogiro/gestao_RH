from django.urls import path
from .views import (FuncionariosList, FuncionarioEdit, FuncionarioDelete,
                    FuncionarioNovo)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='funcionario_list'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='funcionario_edit'),
    path('excluir/<int:pk>/', FuncionarioDelete.as_view(), name='funcionario_delete'),
    path('novo/', FuncionarioNovo.as_view(), name='funcionario_create'),
]