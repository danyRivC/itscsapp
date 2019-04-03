from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
User = get_user_model()
from itscsapp.carrers.models.carrer import Carrer
from itscsapp.events.models.event import EventModel
from itscsapp.blog.models import PostBlog



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/home.html', {'error': 'Error usuario o contraseña ingresados no son correctos',
                                                      'carrers':Carrer.objects.all(),
                                                      'events': EventModel.objects.all(),
                                                      'blogs': PostBlog.objects.all()})
    return render(request, 'core/home.html')


def sign_up(request):
    carrers = Carrer.objects.all()
    events = EventModel.objects.all()
    blogs = PostBlog.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password_confirmation != password:
            return render(request, 'core/home.html', {'error': 'Las contraseñas no coinciden',
                                                      'carrers': carrers,
                                                      'events': events,
                                                      'blogs': blogs})
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            return render(request, 'core/home.html', {'error': 'Username is already in user',
                                                      'carrers': carrers,
                                                      'events': events,
                                                      'blogs': blogs})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('home')
    return render(request, 'core/home.html', {'carrers': carrers,
                                               'events': events,
                                                'blogs': blogs})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



