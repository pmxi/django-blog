from django.shortcuts import render
from .models import Article, Tag


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


def all_tags(request):
    tags = Tag.objects.all()
    context = {
        "tags": tags
    }
    return render(request, 'blog/all_tags.html', context)


def tag(request, tag_name):
    selected_tag = Tag.objects.get(tag_name=tag_name)
    context = {
        "tag": selected_tag,
    }
    return render(request, 'blog/tag.html', context)
