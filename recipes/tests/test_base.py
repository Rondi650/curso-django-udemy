from django.test import TestCase
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = self.make_category(name='Pastel')
        author = self.make_author()
        recipe = self.make_recipe(category, author)

        return super().setUp()

    def make_category(self, name):
        category = Category.objects.create(name=name)
        return category

    def make_author(
            self,
            first_name='XPTO',
            last_name='C3PO',
            username='pqp_pra_la',
            email='user@user',
            password='jafsyuhasfyfas1524'
    ):
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email)
        return user

    def make_recipe(
            self,
            category: Category,
            author: User,
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
        recipe = Recipe.objects.create(
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
        return recipe
