from django.shortcuts import render
from .models import Museo

# Create your views here.

def museos(request):
    museo = Museo.objects.all()
    return render(request,"museobd/museos.html"), {'Museos': museo}