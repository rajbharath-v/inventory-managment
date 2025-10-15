from django.shortcuts import render
from .models import Product
# Create your views here.
def raj(request):
    return render(request,'home.html')
def userDetails(request):
    product=Product.objects.all()
    return render(request,'user.html',{'product':product})
    
