from django.contrib import admin

from .models import Message, BlogPost

admin.site.site_title = "Tushar Gaurav"
admin.site.site_header = "tushgaurav.in | Administration Portal"

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created')

admin.site.register(Message, MessageAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)