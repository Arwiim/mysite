from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post) #The @admin.register() decorator performs the same function as the admin.site.register()
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') #fields displayed
    list_filter = ('status', 'created', 'publish', 'author') #filter the results by the fields
    search_fields = ('title', 'body') #searchable fields
    prepopulated_fields = {'slug': ('title',)} #the slug field is filled in automatically
    raw_id_fields = ('author',)
    date_hierarchy = 'publish' #date hierarchy
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')