from django.views.generic import DetailView, ListView
from .models import *
from itscsapp.comment.forms.comment import CommentForm
from django.views.generic.edit import FormView

class CarrerDetailView(DetailView):
    model = Carrer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['asignatures'] = Asignature.objects.all()
        context['semesters'] = Semester.objects.all()
        context['carrers'] = Carrer.objects.all()
        return context


class AlCarrerView(ListView):
    model = Carrer
    paginate_by = 30
    template_name = 'carrers/all-courses.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context
