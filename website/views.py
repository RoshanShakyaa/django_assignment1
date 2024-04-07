from django.shortcuts import render

# Create your views here.

def homeview(request):
    return render(request, 'website/home.html')

def aboutview(request):
    return render(request, 'website/about.html')

def contactview(request):
    return render(request, 'website/contact.html')
