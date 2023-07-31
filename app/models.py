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
    title = models.CharField(verbose_name="Título", max_length=200, null=False)
    content = RichTextField(verbose_name="Contenido")
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    image = models.ImageField(null=False, blank=False, upload_to="images/post")
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count = models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'posts'
        verbose_name_plural = 'posts'
        ordering = ['title', 'last_updated']

    def __str__(self):
        return self.title


class Comments(models.Model):
    content = models.TextField(verbose_name="Comentario")
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'comments'
        verbose_name_plural = 'comments'


class Subscribe(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'suscribe'
        verbose_name_plural = 'suscribes'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile")
    slug = models.SlugField(max_length=200, unique=True)
    bio = RichTextField(verbose_name="Biografia")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'profiles'
        verbose_name_plural = 'profiles'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return f'{self.first_name} {self.last_name}'


class WebsiteMeta(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    description = models.CharField(verbose_name="Descripcion", max_length=500)
    about = RichTextField(verbose_name="About")

    class Meta:
        verbose_name = 'website metas'
        verbose_name_plural = 'website metas'

    def __str__(self):
        return self.title
