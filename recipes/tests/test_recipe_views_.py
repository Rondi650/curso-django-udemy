
from django import views
from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views

# Django Unit Test


class RecipeViewsTest(TestCase):
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        # print(f'\n', view)
        # print(f'\n', views.category)
        self.assertIs(view.func, views.category)

    def test_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
