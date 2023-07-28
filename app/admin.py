from django.contrib import admin
from app.models import Post, Tag, Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'view_count')
    prepopulated_fields = {'slug': ['title']}
    list_display_links = ('title', 'slug')
    list_filter = ('title', 'slug')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    list_display_links = ('name', 'slug')
    list_filter = ('name', 'slug')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_display_links = ('name', 'email')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentAdmin)
