from django.contrib import admin
from xsxsblog.blog.models import Post,Tag 
import markdown 

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','pub_time']

class TagAdmin(admin.ModelAdmin):	
	list_display = ['name']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
