from django.test import TestCase
from django.urls import reverse

class RecipeUrlsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
class RecipeUrlsTest(TestCase):
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_slug':"sobremesas"})
        self.assertEqual(url, '/sobremesas/')