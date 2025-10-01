from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
  articles = Article.objects.all().order_by('-updated_at')

  context = {
    'articles': articles
  }
  
  return render(request, 'articles/article_list.html', context)

def article_detail(request, slug):
  pass

def article_create(request):
  pass
