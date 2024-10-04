from django.contrib import admin
from newblog.models import blogEnquiry

class blogAdmin(admin.ModelAdmin):
    list_display = ('blog_title' , 'blog_text' , 'blog_file')


# Register your models here.

admin.site.register(blogEnquiry , blogAdmin)

