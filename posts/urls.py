from django.urls import path
from . import views

urlpatterns = [
  # path -> /posts
  path('', views.index, name='index'),
  # path /post/1
  path('<int:post_id>/', views.post, name='post')
]