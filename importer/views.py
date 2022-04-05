from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registeruser(request):

    return render(request, 'importer/registeruser.html', {'form':UserCreationForm()})