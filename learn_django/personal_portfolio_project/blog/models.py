from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	summary = models.CharField(max_length=250, blank=True)
	text = models.TextField()
	url = models.URLField(blank=True)