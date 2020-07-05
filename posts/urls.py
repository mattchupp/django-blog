from django.urls import path, include
from . import views

# giving posts an app name to have namespaced urls in templates
app_name = 'posts'

urlpatterns = [
  # martor app
  path('martor/', include('martor.urls')),
  # path -> /posts
  path('', views.index, name='index'),
  # path -> /post/1/
  path('<int:post_id>/', views.post, name='post')
]