from django.shortcuts import render
from .models import Bb

data = Bb.objects.all()


def index(request):
    return render(request, 'galery/index.html', {})


def galery(request):
    return render(request, 'galery/gal.html', {'data':data})
# Create your views here.
