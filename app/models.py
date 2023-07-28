from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'tags'
        verbose_name_plural = 'tags'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'posts'
        verbose_name_plural = 'posts'
        ordering = ['title', 'last_updated']


class Comments(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')

    class Meta:
        verbose_name = 'comments'
        verbose_name_plural = 'comments'

