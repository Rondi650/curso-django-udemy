from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.


class RecipeURLTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('recipes:home')
        assert url == '/'


@pytest.mark.parametrize('category_id', [1, 2, 3])
def test_category_url_is_correct(category_id):
    url = reverse('recipes:category', kwargs={'category_id': category_id})
    assert url == f'/recipes/category/{category_id}/'
