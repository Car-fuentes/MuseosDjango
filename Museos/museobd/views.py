from django.shortcuts import render
from .models import Museo

# Create your views here.

def museobd(request):
    museo = Museo.objects.all()
    return render(request,"museobd/museos.html"), {'Museo': museo}