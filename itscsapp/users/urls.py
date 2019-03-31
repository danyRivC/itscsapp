from django.urls import path

from itscsapp.users.views import login_view, logout_view, sign_up

app_name = "users"
urlpatterns = [
    path("login/", view=login_view, name='login_view'),
    path("logout/", view=logout_view, name='logout_view'),
    path("signup/", view=sign_up, name='signup_view')
]
