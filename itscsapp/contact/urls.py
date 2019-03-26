from django.urls import path
from itscsapp.contact.views import ContactForm
urlpatterns = [
    path('', ContactForm.as_view(), name='contact'),

]
