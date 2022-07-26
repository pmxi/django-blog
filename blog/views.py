from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
import markdown


# Create your views here.


def index(request):
    context = {
        "articles": Article.objects.order_by('-pub_date')
    }
    return render(request, 'blog/index.html', context)


def article(request, article_slug):
    article = Article.objects.get(slug__exact=article_slug)
    context = {
        "article": article,
    }
    return render(request, 'blog/article.html', context)
