from django.urls import reverse
from recipes.tests.test_base import RecipeTestBase

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
