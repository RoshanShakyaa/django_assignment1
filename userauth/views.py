from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request , 'userauth/register.html')
def log(request):
    return render(request , 'userauth/log.html')