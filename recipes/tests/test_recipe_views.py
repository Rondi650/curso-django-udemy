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

    def test_recipe_search_uses_correct_view_function(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_search_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class RecipeHomeViewDataTest(RecipeTestBase):
    def response_get_home(self):
        return self.client.get(reverse('recipes:home'))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.response_get_home()

        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_home_template_loads_slug(self):
        self.make_recipe()
        response = self.response_get_home()
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.slug, 'teste-slug')

    def test_recipe_home_template_loads_username(self):
        self.make_recipe()
        response = self.response_get_home()
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.author.username, 'pqp_pra_la')

    def test_recipe_home_template_has_content_preparation_time(self):
        self.make_recipe()
        response = self.response_get_home()
        content = response.content.decode('utf-8')

        self.assertIn('10 minutos', content)

    def test_recipe_home_template_has_content_servings_units(self):
        self.make_recipe()
        response = self.response_get_home()
        content = response.content.decode('utf-8')

        self.assertIn('4 pessoas', content)

    def test_recipe_home_template_loads_username_altered(self):
        self.make_recipe(author={'username': 'rondi'})
        response = self.response_get_home()
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.author.username, 'rondi')

    def test_recipe_home_template_loads_category_altered(self):
        self.make_recipe(category={'name': 'Especial'})
        response = self.response_get_home()
        response_content = response.context['recipes'].first()

        self.assertEqual(response_content.category.name, 'Especial')

    def test_dont_show_recipes_not_published(self):
        self.make_recipe(is_published=False)
        response = self.response_get_home()
        response_content = response.context['recipes']

        self.assertEqual(len(response_content), 0)

    def test_dont_show_recipes_not_published_in_the_page(self):
        self.make_recipe(is_published=False)
        response = self.response_get_home()
        content = response.content.decode('utf-8')

        self.assertIn(
            'Sem receitas disponibilizadas aqui.',
            content)


class RecipeCategoryViewDataTest(RecipeTestBase):
    def response_get_category(self, category_id=1):
        return self.client.get(
            reverse('recipes:category', kwargs={'category_id': category_id}))

    def test_recipe_category_template_loads_recipes(self):
        self.make_recipe(category={'name': 'pao'})
        response = self.response_get_category()
        response_content = response.context['recipes']
        self.assertEqual(len(response_content), 1)

    def test_recipe_category_status_code_200(self):
        self.make_recipe(category={'name': 'pao'})
        response = self.response_get_category()
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_status_code_404(self):
        response = self.response_get_category(category_id=999)
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_category_altered(self):
        self.make_recipe(category={'name': 'Especial'})
        response = self.response_get_category()
        response_content = response.context['recipes'].first()
        self.assertEqual(response_content.category.name, 'Especial')

    def test_recipe_category_template_has_data(self):
        self.make_recipe()
        response = self.response_get_category()
        content = response.content.decode('utf-8')
        self.assertIn('Nova Categoria', content)

    def test_category_show_404_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.response_get_category()
        assert response.status_code == 404


class RecipeViewDataTest(RecipeTestBase):
    def response_get_recipe(self, id=1):
        return self.client.get(
            reverse('recipes:recipe', kwargs={'id': id}))

    def test_recipe_template_loads_recipes(self):
        self.make_recipe(category={'name': 'pao'})
        response = self.response_get_recipe()
        response_content = response.context['recipe']
        self.assertEqual(response_content.id, 1)

    def test_recipe_status_code_200(self):
        self.make_recipe(category={'name': 'pao'})
        response = self.response_get_recipe()
        self.assertEqual(response.status_code, 200)

    def test_recipe_status_code_404(self):
        response = self.response_get_recipe(id=999)
        self.assertEqual(response.status_code, 404)

    def test_recipe_template_loads_altered(self):
        self.make_recipe(category={'name': 'Especial'})
        response = self.response_get_recipe()
        response_content = response.context['recipe']
        self.assertEqual(response_content.category.name, 'Especial')

    def test_recipe_template_has_data(self):
        self.make_recipe()
        response = self.response_get_recipe()
        content = response.content.decode('utf-8')
        self.assertIn('Nova Categoria', content)

    def test_recipe_show_404_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.response_get_recipe()
        assert response.status_code == 404


def test_recipe_views_with_pytest():
    # apenas testando uso do pytest
    view_h = resolve(reverse('recipes:home'))
    view_c = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    view_r = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    assert views.home is view_h.func
    assert views.category is view_c.func
    assert views.recipe is view_r.func
