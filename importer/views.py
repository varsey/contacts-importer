import csv
from datetime import datetime
from io import TextIOWrapper
import pandas as pd
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from .models import Contacts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    """homepage. basicaly it's currentcontacts"""
    return render(request, "importer/home.html")


def registeruser(request):
    """User Registration"""
    registration_html = 'importer/registeruser.html'
    if request.method == "GET":
        return render(request, registration_html, {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # check if uname is email
            if '@' in request.POST['username']:
                # if passwords match trying to save user and redirecting him to currentcontacts
                try:
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1']
                    )
                    user.save()
                    login(request, user)
                    return redirect('currentcontacts')

                except IntegrityError:
                    msg = 'That username has been already been taken. Please choose a new username'
                    return render(request, registration_html, {'form': UserCreationForm(), 'error': msg})
            else:
                msg = 'Please use email as your username'
                return render(request, registration_html, {'form': UserCreationForm(), 'error': msg})

        else:
            msg = 'Passwords did not match'
            return render(request, registration_html, {'form': UserCreationForm(), 'error': msg})


def loginuser(request):
    """logins user in to system"""
    auth_html = 'importer/loginuser.html'
    if request.method == "GET":
        return render(request, auth_html, {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            msg = 'Username and password did not match'
            return render(request, auth_html, {'form': AuthenticationForm(), 'error': msg})
        else:
            login(request, user)
            return redirect('contacts')


def logoutuser(request):
    """logs out user"""
    if request.method == "POST":
        logout(request)
        return redirect('home')


def cleartable(request):
    """clears table"""
    if request.method == "POST":
        Contacts.objects.all().delete()
        return redirect('contacts')


def upload_contacts(request):
    """main page with contacts importer and viewer"""
    if request.method == 'POST' and request.FILES['contacts_file']:
        csv_file = TextIOWrapper(request.FILES["contacts_file"].file, encoding='utf-8')
        reader = csv.reader(csv_file)
        _ = next(reader)
        for row in reader:
            Contacts.objects.get_or_create(
                Name=row[0],
                DOB=datetime.strptime(row[1], '%Y-%m-%d'),
                Phone=row[2],
                Address=row[3],
                CreditCard=row[4],
                Franchise=row[5],
                Email=row[6],
            )

    contacts_list = Contacts.objects.order_by("-Email")
    page = request.GET.get('page', 1)
    paginator = Paginator(contacts_list, 3)
    try:
        thecontacts = paginator.page(page)
    except PageNotAnInteger:
        thecontacts = paginator.page(1)
    except EmptyPage:
        thecontacts = paginator.page(paginator.num_pages)

    return render(request, 'importer/contacts.html',  {'contacts': thecontacts})
