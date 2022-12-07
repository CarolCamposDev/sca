from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView, ListView
from .models import Porte, Animal, Especie, Cliente
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView

#views pdf
from django_weasyprint import WeasyTemplateView


from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML

#viewforms
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContatoForm
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'base.html'

class SobreView(TemplateView):
    template_name = 'about-us.html'

class PortesView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super(PortesView, self).get_context_data(**kwargs)
        context['portes'] = Porte.objects.order_by('nome').all()
        return context

class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['animais'] = Animal.objects.order_by('?').all()
        return context

class AnimalDetalheView(ListView):
    template_name = 'course-detail.html'
    paginate_by = 5
    ordering = 'nome'
    model = Especie

    def get_context_data(self, **kwargs):
        context = super(AnimalDetalheView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['curso'] = Animal.objects.filter(id=id).first
        return context

    def get_queryset(self, **kwargs):
        id = self.kwargs['id']
        return Especie.objects.filter(curso_id=id)


class DadosGraficoClientesView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = Animal.objects.order_by('id')
        for animal in queryset:
            labels.append(animal.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Animal.objects.order_by('id').annotate(total=Count('cliente'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado


class RelatorioClientesView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        cliente = Cliente.objects.order_by('nome').all()

        html_string = render_to_string('relatorio-clientes.html', {'clientes': Cliente})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-clientes.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-clientes.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-clientes.pdf"'
        return response


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso', extra_tags='success')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar e-mail', extra_tags='danger')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)
