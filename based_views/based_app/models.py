from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Poem(models.Model):
	count = models.IntegerField(default=0) 
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100,default="")
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Poem, self).save(*args, **kwargs)
	def __str__(self):
		return self.title
	def update_counter(self):
		self.count = self.count+1

class tasks(models.Model):
	task_id = models.IntegerField()
	name = models.CharField(max_length=100)
