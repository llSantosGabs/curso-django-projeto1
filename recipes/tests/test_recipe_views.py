from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
     view = resolve(reverse('recipes:home'))
     self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
     view = resolve(reverse('recipes:category', kwargs={'category_slug':"sobremesas"}))
     self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404_if_no_recipes_found(self):
     response = self.client.get(reverse('recipes:category', kwargs={'category_slug':"sobremesass"}))
     self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
     view = resolve(reverse('recipes:recipe', kwargs={'id':1}))
     self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_return_status_code_200_OK(self):
      response = self.client.get(reverse('recipes:home'))
      self.assertEqual(response.status_code, 200)

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
      response = self.client.get(reverse('recipes:home'))
      self.assertIn('No Recipes Found Here', response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
      category = Category.objects.create(name='Category')
      assert 1 == 1