from django.shortcuts import render
from .models import product, techType, Review 

def index(request):
    return render(request, 'club\index.html')

    def products(request):
        product_list=product.objects.all()
        return render(request, 'club/product.html', {'product_list': product_list})
 
