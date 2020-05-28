from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all() #Pegamos os objetos do Project e salvamos na variavel projects
    return render(request, 'portfolio/home.html',{'projects':projects})