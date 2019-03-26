from django.views.generic import TemplateView
from itscsapp.carrers.models import *


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


