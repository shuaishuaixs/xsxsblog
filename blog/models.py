from django.db import models

# Create your models here.

from django.db import models
from markdown import markdown

class Tag(models.Model):
	name = models.CharField(max_length=100,unique=True)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=30)
	tags = models.ManyToManyField(Tag)
	#content = models.TextField()
	content = models.TextField() 
	content_markdown = models.TextField(editable=False,blank=True,null=True)
	pub_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']

	def save(self):
		self.content_markdown = markdown(self.content,['codehilite'])
		#self.content_markdown = markdown(self.content,extensions = ['codehilite'])
		super(Post,self).save()
