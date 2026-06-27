from unittest import TestCase
from django.urls import reverse
import pytest


class RecipeURLTest(TestCase):
    # Django Unit Test
    def test_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')  # modo 1

    def test_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        assert url == '/recipes/1/'  # modo 2

    def test_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        assert url == '/recipes/category/1/'


# pytest enviando multiplos ids em loop
@pytest.mark.parametrize('category_id', [1, 2, 3])
def test_category_multiple_ids_url_is_correct(category_id):
    url = reverse('recipes:category', kwargs={'category_id': category_id})
    assert url == f'/recipes/category/{category_id}/'
