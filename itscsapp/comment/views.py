from django.shortcuts import render
from django.shortcuts import render,redirect
from itscsapp.comment.forms.comment import CommentForm
from django.http import HttpResponseBadRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from itscsapp.carrers.models import Carrer



def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
        return redirect(comment.carrer.get_absolute_url())
    else:
        return HttpResponse('Algo salio mal')
