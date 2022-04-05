from django.shortcuts import render


def registeruser(request):
    return render(request, 'importer/registeruser.html')