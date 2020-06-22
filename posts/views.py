from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

# Create your views here.
def index(request): 

  # get list of posts and sort by date
  latest_posts = Post.objects.order_by('post_date')

  # context for latest_posts in template
  context = {
    'latest_posts': latest_posts,
  }

  # render the request with template polls/index.html 
  # with context of latest posts
  return render(request, 'posts/index.html', context)


def post(request, post_id): 
  response = "Here is the page for %s."

  return HttpResponse(response % post_id)