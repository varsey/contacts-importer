from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def registeruser(request):
    """User Registration"""
    registeration_html = 'importer/registeruser.html'
    if request.method == "GET":
        return render(request, registeration_html, {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # if passwords match trying to save user
            try:
                User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                User.save()
            except IntegrityError:
                msg = 'That username has been already been taken. Please choose a new username'
                return render(request, registeration_html, {'form': UserCreationForm(), 'error': msg})
        else:
            msg = 'Passwords did not match'
            return render(request, registeration_html, {'form': UserCreationForm(), 'error': msg})
