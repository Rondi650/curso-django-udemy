from recipes.models import Category
from recipes.tests.test_base import RecipeTestBase


class ModelsPrintTest(RecipeTestBase):
    def test_return_recipe(self):
        response = self.make_recipe()
        print(response)

    def test_return_category(self):
        response = Category('teste')
        print(response)
