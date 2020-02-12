from django.urls import path
from .views import (DepartamentosList, DepartamentoEdit, DepartamentoDelete,
                    DepartamentoNovo)

urlpatterns = [
    path('list/', DepartamentosList.as_view(), name='departamento_list'),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name='departamento_edit'),
    path('excluir/<int:pk>/', DepartamentoDelete.as_view(), name='departamento_delete'),
    path('novo/', DepartamentoNovo.as_view(), name='departamento_create'),
]