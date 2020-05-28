from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] # Ordenar pelo mais recente e mostrar os ultimos 5
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # pk = primary key. Faz a busca para validar se o blog existe, e da erro caso nao encontre
    return render(request, 'blog/detail.html',{'blog':blog}) # Criamos um dicionarios e pegamos todos os blog existentes
