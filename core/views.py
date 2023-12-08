from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def arte(request):
    return render(request,"core/arte.html")

def ciencias(request):
    return render(request, "core/ciencias.html")

def historia(request):
    return render(request, "core/historia.html")

def tematicos(request):
    return render(request, "core/tematicos.html")

def contacto(request):
    return render(request, "core/contacto.html")

def otros(request):
    return render(request, "core/otros.html" )


