from django.db import models

# Create your models here.
class Post(models.Model): 
  post_title = models.CharField(max_length=200)
  post_content = models.TextField(max_length=None, serialize=True)
  post_date = models.DateTimeField(auto_now=True)