from django.contrib import admin

# Register your models here.


from .models import BlogPosts

class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author','created_at','updated_at','is_published')
    list_display_links = ('id', 'title')
    search_fields = ('id','title')

admin.site.register(BlogPosts, BlogPostsAdmin)
