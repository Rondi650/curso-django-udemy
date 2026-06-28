from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from recipes.tests.test_base import RecipeTestBase
from rich import print



class RecipeViewsTest(TestCase):
    # Django Unit Test

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_home_view_return_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        assert response.status_code == 200

    def test_category_view_return_404_if_no_recipes_found(self):
        view = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(view.status_code, 404)

    def test_recipe_view_return_404_if_no_recipes_found(self):
        view = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(view.status_code, 404)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Sem receitas disponibilizadas aqui.',
            response.content.decode('utf-8')
        )


class RecipeHomeViewDataTest(RecipeTestBase):
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_home_template_loads_slug(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.slug, 'teste-slug')

    def test_recipe_home_template_loads_username(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.author.username, 'pqp_pra_la')

    def test_recipe_home_template_has_content_preparation_time(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn('10 minutos', content)

    def test_recipe_home_template_has_content_servings_units(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertIn('4 pessoas', content)

    def test_recipe_home_template_loads_username_altered(self):
        self.make_recipe(author={'username': 'rondi'})
        response = self.client.get(reverse('recipes:home'))
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.author.username, 'rondi')

    def test_recipe_home_template_loads_category_altered(self):
        self.make_recipe(category={'name': 'Especial'})
        response = self.client.get(reverse('recipes:home'))
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.category.name, 'Especial')





def test_recipe_views_with_pytest():
    # apenas testando uso do pytest
    view_h = resolve(reverse('recipes:home'))
    view_c = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    view_r = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    assert views.home is view_h.func
    assert views.category is view_c.func
    assert views.recipe is view_r.func
