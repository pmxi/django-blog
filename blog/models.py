from django.db import models
from markdown import markdown


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    pub_date = models.DateTimeField()
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def render_content_markdown(self):
        return markdown(self.content)
