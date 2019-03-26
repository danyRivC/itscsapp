from django.urls import path
from .views import ResearchesViews, ResearchDetail
urlpatterns=[
    path('all-research/', ResearchesViews.as_view(), name='allResearches'),
    path('research/<int:pk>/<slug:slug>/', ResearchDetail.as_view(), name='researchDetail'),
]
