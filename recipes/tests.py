from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class RecipeURLTest(TestCase):
    def test_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        assert home_url == '/'
