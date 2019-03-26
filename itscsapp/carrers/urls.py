from django.urls import path
from itscsapp.carrers.views import *

urlpatterns = [
    path('<int:pk>/<slug:slug>/', CarrerDetailView.as_view(), name='courseDetail'),
    path('', AlCarrerView.as_view(), name='allCarrers')
]
