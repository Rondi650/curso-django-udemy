from recipes.models import Category
from recipes.tests.test_base import RecipeTestBase
import pytest


class RecipeModelStrTest(RecipeTestBase):
    def test_recipe_str_method(self):
        response = self.make_recipe()
        print(response)

    def test_category_str_method(self):
        response = Category('teste')
        print(response)

    @pytest.mark.skip(reason='aprendizado')
    def test_that_will_fail(self):
        self.fail('Fail on purpose, for education knowledge')


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
