from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'global/home.html')

def contact(request):
    return render(request, 'example/contact.html')

def about(request):
    return render(request, 'example/about.html')
