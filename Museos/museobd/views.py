from django.shortcuts import render
from .models import Museo

# Create your views here.

def museos(request):
    museos = Museo.objects.all()
    return render(request,"museos/museos.html"), {'Museos': museos}