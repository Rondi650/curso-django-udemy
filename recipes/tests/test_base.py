from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
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
        return super().setUp()
