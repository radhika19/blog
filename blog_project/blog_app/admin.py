from django.contrib import admin
from .models import Blog, Paragraph, Comment

class BlogAdmin(admin.ModelAdmin):
   model = Blog
   exclude = ['seq']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Paragraph)
admin.site.register(Comment)
