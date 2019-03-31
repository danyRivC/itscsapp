from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import AdmisionCarrerForm, AdmisionEventForm
from django.urls import reverse_lazy
from itscsapp.carrers.models import Carrer
from django.views.generic import DetailView
from itscsapp.events.models.event import EventModel
from django.shortcuts import HttpResponse


class AdmisionCarrerView(FormView):
    form_class = AdmisionCarrerForm
    template_name = 'admision/admission.html'

    def get_success_url(self):
        return reverse_lazy('admision')+'?ok'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()

        return context


class AdmisionEvent(DetailView):
    model = EventModel
    template_name = 'admision/event-register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_register'] = AdmisionEventForm
        context['carrers'] = Carrer.objects.all()
        return context


def admision_event(request):
    if request.method == 'POST':
        form = AdmisionEventForm(request.POST)
        if form.is_valid():
            event_adminsion = form.save(commit=False)
            event_adminsion.save()
        return redirect(event_adminsion.event.get_absolute_url())
    else:
        return HttpResponse('Algo salio mal')
