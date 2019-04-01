from django.views.generic import DetailView, ListView
from .models import *
from itscsapp.comment.forms.comment import CommentForm
from django.shortcuts import render
from itscsapp.events.models.event import EventModel
class CarrerDetailView(DetailView):
    model = Carrer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['asignatures'] = Asignature.objects.all()
        context['semesters'] = Semester.objects.all()
        context['carrers'] = Carrer.objects.all()
        context['events'] = EventModel.objects.all()
        return context


class AlCarrerView(ListView):
    model = Carrer
    paginate_by = 30
    template_name = 'carrers/all-courses.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


def searchCarrer(request, query):
    query = request.GET['query']
    carrers = Carrer.objects.filter( title__icontains=query)
    if carrers:
        return render(request=request, template_name='carrers/courses-search.html', context={'carrers':carrers})
    else:
        return render(request, 'carrers/all-courses.html', {'error':'No se encuentra el producto'})
