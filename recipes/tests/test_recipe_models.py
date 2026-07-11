from recipes.models import Category
from recipes.tests.test_base import RecipeTestBase
from django.core.exceptions import ValidationError
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

    # assercao de raise com pytest
    def test_recipe_raises_error_if_tatle_has_more_than_65_chars(self):
        with pytest.raises(ValidationError):
            self.recipe.title = 'a' * 70
            self.recipe.full_clean()

    # assercao de raise com unittest
    def test_recipe_raises_error_if_description_has_more_than_165_chars(self):
        with self.assertRaises(ValidationError):
            self.recipe.description = 'a' * 170
            self.recipe.full_clean()

    # teste de raise em lote
    def test_recipe_fileds_max_lenght(self):
        fields = [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ]

        # subtest com context manager permite ver todos erros do loop
        for field, max_lenght in fields:
            with self.subTest(field=field, max_lenght=max_lenght):
                with self.assertRaises(ValidationError):
                    setattr(self.recipe, field, 'A' * (max_lenght + 0))
                    self.recipe.full_clean()
