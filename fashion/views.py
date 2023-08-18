from django.shortcuts import render
from .models import Outfit

# Create your views here.
def index(request):
    context = {
        "outfits": Outfit.objects.order_by('-date')
    }
    return render(request, 'fashion/index.html', context)

def about(request):
    context = {}
    return render(request, 'fashion/about.html', context)

def contact(request):
    context = {}
    return render(request, 'fashion/contact.html', context)