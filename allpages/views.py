from django.shortcuts import render

# Create your views here.
# Here I use functions, but I could also use classes.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# The templates folder is assumed !!

def home_view(request):
    return render(request, 'allpages/index.html' , {'title': 'Home'})

def about_view(request):
    return render(request, 'allpages/about.html', {'title': 'About us'} )

def privacy_view(request):
    return render(request, 'allpages/privacy.html', {'title': 'Privacy Policy'})
