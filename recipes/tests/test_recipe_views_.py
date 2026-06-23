
from django import views
from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from rich import print

# Django Unit Test


class RecipeViewsTest(TestCase):
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        # # categoria = reverse('recipes:category', kwargs={'category_id': 1})
        # view2 = resolve(f'/recipes/category/5/')
        # print(f'\n', view)
        # print(f'\n', view2)
        # print(f'\n', views.category)
        self.assertIs(view.func, views.category)

    def test_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)


def test_recipe_views_with_pytest():
    # apenas testando uso do pytest
    view_h = resolve(reverse('recipes:home'))
    view_c = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    view_r = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    assert views.home is view_h.func
    assert views.category is view_c.func
    assert views.recipe is view_r.func
