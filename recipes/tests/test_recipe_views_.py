from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from rich import print
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


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


class RecipeViewTestWithMock(TestCase):
    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Categoria Teste')
        user = User.objects.create_user(first_name='XPTO',
                                        last_name='C3PO',
                                        username='pqp_pra_la',
                                        password='jafsyuhasfyfas1524',
                                        email='user@user')
        recipe = Recipe.objects.create(
            title='teste',
            description='descricao teste',
            slug='teste-slug',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=4,
            servings_unit='pessoas',
            preparation_steps='Passo 1\nPasso 2',
            preparation_steps_is_html=False,
            created_at='2026-06-01 00:00:00',
            updated_at='2026-06-01 00:00:00',
            is_published=True,
            category=category,
            author=user
        )

        response = self.client.get(reverse('recipes:home'))
        response_content = response.context['recipes'].first()
        # print(response_content.__dict__)
        content = response.content.decode('utf-8')
        # print(content)

        self.assertEqual(len(response.context['recipes']), 1)
        self.assertEqual(response_content.slug, 'teste-slug')
        self.assertIn('pessoas', content)

        # print(category)
        # print(user.__dict__)
        # print(recipe.__dict__)
        # print(recipe)


def test_recipe_views_with_pytest():
    # apenas testando uso do pytest
    view_h = resolve(reverse('recipes:home'))
    view_c = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    view_r = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    assert views.home is view_h.func
    assert views.category is view_c.func
    assert views.recipe is view_r.func
