from unicodedata import category

from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(
            self,
            name='Nova Categoria'
    ):
        return Category.objects.create(
            name=name)

    def make_author(
            self,
            first_name='XPTO',
            last_name='C3PO',
            username='rondinelle nunes de oliveira',
            email='user@user',
            password='jafsyuhasfyfas1524'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email)

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='pao'),
            author=self.make_author(username='dart'),
            title='teste',
            description='descricao teste',
            slug='teste-slug-a',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=4,
            servings_unit='pessoas',
            preparation_steps='Passo 1\nPasso 2',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def make_recipe(
            self,
            category=None,
            author=None,
            title='teste',
            description='descricao teste',
            slug='teste-slug',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=4,
            servings_unit='pessoas',
            preparation_steps='Passo 1\nPasso 2',
            preparation_steps_is_html=False,
            is_published=True,

    ):
        if category is None:
            category = self.make_category()
        elif isinstance(category, dict):
            category = self.make_category(**category)

        if author is None:
            author = self.make_author()
        elif isinstance(author, dict):
            author = self.make_author(**author)

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            category=category,
            author=author
        )
