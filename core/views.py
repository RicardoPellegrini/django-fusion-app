from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Feature
from .forms import ContatoForm

class IndexView(FormView):
  template_name = 'index.html'
  form_class = ContatoForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['servicos'] = Servico.objects.order_by('?').all()
    context['funcionarios'] = Funcionario.objects.order_by('?').all()
    context['features_left'] = Feature.objects.all()[0:(len(Feature.objects.all())//2)]
    context['features_right'] = Feature.objects.all()[(len(Feature.objects.all())//2):]
    return context

  def form_valid(self, *args, **kwargs):
    form.send_mail()
    messages.success(self.request, 'E-Mail enviado com sucesso')

    return super(IndexView, self).form_valid(form, *args, **kwargs)

  def form_invalid(self, *args, **kwargs):
    messages.error(self.request, 'Erro ao enviar e-mail')

    return super(IndexView, self).form_invalid(form, *args, **kwargs)



