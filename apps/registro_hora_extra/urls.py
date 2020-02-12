from django.urls import path
from .views import (HoraExtraList, HoraExtraEdit, HoraExtraNovo,
                    HoraExtraDelete)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='hora_extra_list'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='hora_extra_edit'),
    path('excluir/<int:pk>/', HoraExtraDelete.as_view(), name='hora_extra_delete'),
    path('novo/', HoraExtraNovo.as_view(), name='hora_extra_create')
]