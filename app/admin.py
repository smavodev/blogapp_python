from django.contrib import admin
from app.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')
    list_filter = ('title', 'slug')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    list_filter = ('name', 'slug')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
