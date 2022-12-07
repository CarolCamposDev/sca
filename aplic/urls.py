

from django.urls import path

from .views import IndexView, SobreView, PortesView, AnimalDetalheView, DadosGraficoClientesView, RelatorioClientesView, ContatoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('portes/', PortesView.as_view(), name='portes'),
    path('animal-detalhe/<int:id>/', AnimalDetalheView.as_view(), name='animal-detalhe'),
    path('dados-grafico-clientes/', DadosGraficoClientesView.as_view(), name='dados-grafico-clientes'),
    path('relatorio-clientes/', RelatorioClientesView.as_view(), name='relatorio-clientes'),
    path('contato/', ContatoView.as_view(), name='contato'),

]
