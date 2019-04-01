from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from itscsapp.carrers.models import Carrer
from itscsapp.about.models import Awards, Department, Facility


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


class DepartmentViews(ListView):
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


class AwardsView(ListView):
    model = Awards

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'about/deparment_detial.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context

class AllFacielieties(ListView):
    model = Facility
    template_name = 'about/facilities.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context


class FacilityView(DetailView):
    model = Facility
    template_name = 'about/facilities-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context



