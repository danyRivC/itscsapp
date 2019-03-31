from django.urls import path
from .views import AdmisionCarrerView, AdmisionEvent, admision_event
urlpatterns = [
    path('admision/', AdmisionCarrerView.as_view(), name='admision'),
    path('admision-event/<int:pk>/<slug:slug>/', AdmisionEvent.as_view(), name='admision-event'),
    path('admision-register', admision_event, name='admision_event_register')
]
