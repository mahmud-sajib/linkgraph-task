from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Article, Writer

"""Testing views"""
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    # Test index view
    def test_index_view(self):
        response = self.client.post(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    

    