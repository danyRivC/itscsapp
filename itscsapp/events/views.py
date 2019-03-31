from django.shortcuts import render
from django.views.generic import DetailView, ListView
from itscsapp.events.models.event import EventModel
from itscsapp.carrers.models import Carrer
from itscsapp.admision.forms import AdmisionEventForm

class AllEventsViews(ListView):
    model = EventModel
    template_name = 'events/events.html'
    paginate_by = 20
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


class EventDetailView(DetailView):
    model = EventModel
    template_name = 'events/events-detail.html'

