from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.
class IndexView(generic.ListView):
    template_name = "pilotapp/home.html"
    model = Blog
