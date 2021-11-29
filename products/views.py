from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    products=Products.objects.all()
       
    return render(request,'index.html',{'products':products})
   
def indexnew(request):
    return HttpResponse('new page of the products loaded thank you!')

