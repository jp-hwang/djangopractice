from django.shortcuts import render
from .models import Shop

def index(request):
    return render(request, 'baemin/index.html', {
        'shop_list' : Shop.objects.all(),
    })
