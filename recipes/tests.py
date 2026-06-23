from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
import pytest

# Unittest Django


class RecipeURLTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('recipes:home')
        assert url == '/'

    def test_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        assert url == '/recipes/1/'

    def test_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        assert url == '/recipes/category/1/'


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

# pytest enviando multiplos ids em loop


@pytest.mark.parametrize('category_id', [1, 2, 3])
def test_category_multiple_ids_url_is_correct(category_id):
    url = reverse('recipes:category', kwargs={'category_id': category_id})
    assert url == f'/recipes/category/{category_id}/'
