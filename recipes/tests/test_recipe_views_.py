from django import views
from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from rich import print


class RecipeViewsTest(TestCase):
    # Django Unit Test
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

    def test_home_view_return_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        assert response.status_code == 200

    def test_category_return_status_code_200(self):
        response = self.client.get('/recipes/category/5/')
        assert response.status_code == 200

    def test_recipe_view_return_status_code_200(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        assert response.status_code == 200

    def test_recipe_home_view_loads_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')


def test_recipe_views_with_pytest():
    # apenas testando uso do pytest
    view_h = resolve(reverse('recipes:home'))
    view_c = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    view_r = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    assert views.home is view_h.func
    assert views.category is view_c.func
    assert views.recipe is view_r.func
