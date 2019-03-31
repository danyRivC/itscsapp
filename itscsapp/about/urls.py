from django.urls import path
from .views import *


urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('awards/', AwardsView.as_view(), name='awards'),
    path('departments/', DepartmentViews.as_view(), name='departments'),
    path('department/<int:pk>/<slug:slug>', DepartmentDetailView.as_view(), name='department_detail'),
    path('facilities/', AllFacielieties.as_view(), name='allFacilities'),
    path('facility/<int:pk>/<slug:slug>/', FacilityView.as_view(), name='facility'),
]

