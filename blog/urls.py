from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:article_slug>/', views.article, name='article'),
    path('tags', views.all_tags, name='all_tags'),
    path('tags/<tag_name>', views.tag, name='tag'),
]
