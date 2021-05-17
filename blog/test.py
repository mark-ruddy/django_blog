from django.test import TestCase
from blog.models import Post

class BlogTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='testing', author=1, tags='tech')
    
    def test_can_get_blog(self):
        testing_blog = Post.objects.get(title='testing')
        self.assertEqual(testing_blog.tags, 'tech')

