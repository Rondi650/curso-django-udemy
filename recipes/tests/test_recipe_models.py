from recipes.models import Category
from recipes.tests.test_base import RecipeTestBase


class RecipeModelStrTest(RecipeTestBase):
    def test_recipe_str_method(self):
        response = self.make_recipe()
        print(response)

    def test_category_str_method(self):
        response = Category('teste')
        print(response)
