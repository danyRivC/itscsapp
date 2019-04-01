from django.views.generic import ListView, DetailView
from .models import Research
from itscsapp.carrers.models import Carrer
from itscsapp.events.models.event import EventModel
from itscsapp.blog.models import PostBlog

class ResearchesViews(ListView):
    model = Research
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        context['events'] = EventModel.objects.all()
        context['blogs'] = PostBlog.objects.all()
        return context

class ResearchDetail(DetailView):
    model = Research
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        context['events'] = EventModel.objects.all()
        context['blogs'] = PostBlog.objects.all()
        return context

