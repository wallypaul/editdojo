from django.db import models

# Create your models here.
class TodoItem(models.Model):
	"""docstring for ClassName"""
	content = models.TextField()
	