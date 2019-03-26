from django.urls import path
from itscsapp.comment import views as commentViews

urlpatterns = [
    path('create-comment/', commentViews.create_comment, name='create_comment'),
]
