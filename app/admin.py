from django.contrib import admin
from app.models import Post, Tag, Comments, Subscribe


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'view_count', 'is_featured', 'modified_date')
    prepopulated_fields = {'slug': ['title']}
    list_display_links = ('title', 'slug')
    list_filter = ('title', 'slug')
    readonly_fields = ('created_date', 'modified_date')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    list_display_links = ('name', 'slug')
    list_filter = ('name', 'slug')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'parent')
    list_display_links = ('name', 'email')


class SuscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    list_display_links = ('email', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Subscribe)

