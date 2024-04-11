from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'anime_name', 'author', 'post_date','is_public')
    list_display_links = ('id', 'anime_name')
    search_fields = ('anime_name', 'author')
    list_per_page = 10
    list_editable = ('is_public',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Category)