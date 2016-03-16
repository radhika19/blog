from django.conf.urls import url
from blog_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [ url(r'^api/blogs/$', views.blogs_list), 
                url(r'^api/blogs/(?P<pk>[0-9]+)$', views.blog_list), 
	]

urlpatterns = format_suffix_patterns(urlpatterns)
