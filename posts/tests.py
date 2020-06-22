from django.test import TestCase
from django.urls import reverse
from django.test import Client


def create_post(post_title):
  return Post.objects.create(post_title=post_title)

# Create your tests here.
class PostsViewTests(TestCase): 

  def test_future_post(self): 
    url = reverse('posts:post', args=(future_post.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)
  
  def test_past_post(self): 
    past_post = create_post(post_title='Past Post')
    url = reverse('posts:post', args=(past_post.id,))
    response = self.client.get(url)
    self.assertContainer(response, past_post.post_title)