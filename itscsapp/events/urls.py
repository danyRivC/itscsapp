from django.urls import path
from .views import AllEventsViews, EventDetailView
urlpatterns = [
    path('events/', AllEventsViews.as_view(), name='allEvents'),
    path('event/<int:pk>/<slug:slug>', EventDetailView.as_view(), name='eventDetail'),

]
