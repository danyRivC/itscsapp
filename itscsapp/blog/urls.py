from django.urls import path
from .views import *

urlpatterns = [
    path('blog', AllPostsBlog.as_view(), name='blog'),
    path('blog/<int:pk>/<slug:slug>', PostBlogDetail.as_view(), name='detial_blog'),
]
