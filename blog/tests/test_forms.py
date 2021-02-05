from django.test import SimpleTestCase
from blog.forms import ArticleCreationForm

"""Testing forms"""
class TestForms(SimpleTestCase):

    # Test if Article Form contains data
    def test_article_form_invalid_data(self):
        form = ArticleCreationForm(data={
            'title':'Title One',
            'content':'Content One'
        })

        self.assertTrue(form.is_valid())

    # Test if Article Form contains no data
    def test_article_form_invalid_data(self):
        form = ArticleCreationForm(data={})
        self.assertFalse(form.is_valid())


