from django.contrib import admin
from .models import Blog, Paragraph, Comment

admin.site.register(Blog)
admin.site.register(Paragraph)
admin.site.register(Comment)
