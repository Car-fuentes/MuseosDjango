from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/home.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def museos(request):
    return render(request,"core/museos.html")

def contacto(request):
    return render(request, "core/contacto.html")




