from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = self.make_category(name='Pastel')
        author = self.make_author()
        recipe = self.make_recipe(category, author)

        return super().setUp()

    def make_category(self, name='Categoria teste'):
        category = Category.objects.create(name=name)
        return category

    def make_author(self):
        user = User.objects.create_user(
            first_name='XPTO',
            last_name='C3PO',
            username='pqp_pra_la',
            password='jafsyuhasfyfas1524',
            email='user@user')
        return user

    def make_recipe(self, category, author):
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
            author=author
        )
        for i in range(2):
            return recipe
