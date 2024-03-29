from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from .models import Nieruchomosci

def lista_nieruchomosci(request):
    nieruchomosci = Nieruchomosci.objects.all()
    return render(request, 'lista_nieruchomosci.html', {'nieruchomosci': nieruchomosci})

# Create your views here.
def home(request):
    return HttpResponse("hellow")