from django.urls import resolve, reverse
from recipes import views
from recipes.tests.test_base import RecipeTestBase
from pprint import pprint
from unittest.mock import patch


class RecipeHomeViewDataTest(RecipeTestBase):
    # Django Unit Test

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_home_view_return_status_code_200(self):
        response = self.client.get(reverse('recipes:home'))
        assert response.status_code == 200

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Sem receitas disponibilizadas aqui.',
            response.content.decode('utf-8')
        )

    def response_get_home(self):
        return self.client.get(reverse('recipes:home'))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.response_get_home()

        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_home_template_loads_slug(self):
        self.make_recipe()
        response = self.response_get_home()
        response_content = response.context['recipes'].object_list[0]

        self.assertEqual(response_content.slug, 'teste-slug')

    def test_recipe_home_template_loads_username(self):
        self.make_recipe()
        response = self.response_get_home()
        response_content = response.context['recipes'].object_list[0]

        self.assertEqual(response_content.author.username,
                         'rondinelle nunes de oliveira')

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
        # pprint('*'*50)
        # pprint(response.context['recipes'].object_list[0].__dict__)
        response_content = response.context['recipes'].object_list[0]

        self.assertEqual(response_content.author.username, 'rondi')

    def test_recipe_home_template_loads_category_altered(self):
        self.make_recipe(category={'name': 'Especial'})
        response = self.response_get_home()
        response_content = response.context['recipes'].object_list[0]

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

    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author': {'username': f'u{i}'}}
            pprint(kwargs)
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=4):
            response = self.client.get(reverse('recipes:home'))
            pprint(response)
            recipes = response.context['recipes']
            pprint(recipes)
            paginator = recipes.paginator
            pprint(paginator)

            self.assertEqual(paginator.num_pages, 4)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)