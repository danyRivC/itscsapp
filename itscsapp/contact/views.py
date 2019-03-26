from django.views.generic.edit import FormView
from itscsapp.contact.forms.contactForm import ContactForm
from django.urls import reverse_lazy
from itscsapp.carrers.models import Carrer


class ContactForm(FormView):
    form_class = ContactForm
    template_name = 'contact/contact-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrers'] = Carrer.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contact')+'?ok'
