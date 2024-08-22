from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    #this is a way to use data directly from here by making dictionary...    
    return render(request, "index.html")

def about_us(request):
    return render(request, "shop-listing.html")

def shop_list(request):
    return render(request, "shop-listing.html")