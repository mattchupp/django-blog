from django.db import models
from martor.models import MartorField

# Create your models here.

# Model for Posts
class Post(models.Model): 
  post_title = models.CharField(max_length=200)
  # post_content = models.TextField(max_length=None, serialize=True)
  post_content = MartorField()
  post_date = models.DateTimeField(auto_now=True)

  # Set a nicer title for posts in admin console 
  def __str__(self): 
    return self.post_title