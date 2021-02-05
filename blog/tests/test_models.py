from django.test import TestCase
from blog.models import Article, Writer
from django.contrib.auth.models import User

"""Testing models"""
class TestModels(TestCase):
    
    # Check if the article owner is the writer
    def test_article_owner_is_writer(self):
        article = Article.objects.create(title="Title One")
        user = User.objects.create(username="mark")
        article_owner = Writer.objects.create(name=user)
        article_owner.article_writer.add(article)
        
        self.assertEqual(article.written_by, article_owner)