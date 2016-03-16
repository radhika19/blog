from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    seq = models.CharField(blank=True, max_length = 500, default='[]')
	
    def __str__(self):
	return self.title

class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog)
    text = models.TextField()
	
    def __str__(self):
	return self.blog.title + str(self.id)
	
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=400)
    paragraph = models.ForeignKey(Paragraph)

    def __unicode__(self):
        return str(self.paragraph.blog.title)+str(self.paragraph.id) + str(self.id)
