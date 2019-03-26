from django.urls import path
from .views import *


urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('awards/', AwardsView.as_view(), name='awards'),
    path('departments/', DepartmentViews.as_view(), name='departments'),
    path('<int:pk/><slug:slug>', DepartmentDetailView.as_view(), name='department_detail'),

]
