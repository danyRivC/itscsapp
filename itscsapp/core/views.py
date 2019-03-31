from django.views.generic import TemplateView
from itscsapp.carrers.models import *
from itscsapp.events.models.event import EventModel
from itscsapp.blog.models import PostBlog
class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        context['events'] = EventModel.objects.all()
        context['blogs'] = PostBlog.objects.all()
        return context


