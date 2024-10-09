from django.urls import path
from .views import HistoricoAtividadeListCreateView

urlpatterns = [
    path('historico-atividade/', HistoricoAtividadeListCreateView.as_view(), name='historico_atividade_list_create'),
]
