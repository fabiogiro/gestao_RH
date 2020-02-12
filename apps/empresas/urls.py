from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='empresa_create'),
    path('edit/<int:pk>/', EmpresaEdit.as_view(), name='empresa_edit'),
]