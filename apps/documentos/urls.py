from django.urls import path
from .views import DocumentoCreate #, DocumentoDelete

urlpatterns = [
    path('novo/<int:funcionario.id>/', DocumentoCreate.as_view(), name='documento_create'),
#    path('delete', DocumentoDelete.as_view(), name='documento_delete'),
]