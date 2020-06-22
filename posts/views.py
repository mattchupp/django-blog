from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
  # shortcut - get the post and if 404 return not found
  post = get_object_or_404(Post, pk=post_id)
  # render post with posts/post.html template
  return render(request, 'posts/post.html', {'post': post})
