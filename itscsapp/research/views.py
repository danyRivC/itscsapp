from django.views.generic import ListView, DetailView
from .models import Research
class ResearchesViews(ListView):
    model = Research

class ResearchDetail(DetailView):
    model = Research

