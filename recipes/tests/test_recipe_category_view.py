from django.urls import reverse, resolve
from recipes import views
from recipes.tests.test_base import RecipeTestBase

class RecipeCategoryViewDataTest(RecipeTestBase):
    def response_get_category(self, category_id=1):
        return self.client.get(
            reverse('recipes:category', kwargs={'category_id': category_id}))
        
    def test_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
        
    def test_category_view_return_404_if_no_recipes_found(self):
        view = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(view.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        self.make_recipe(category={'name': 'pao'})
        response = self.response_get_category()
        response_content = response.context['recipes']
        self.assertEqual(len(response_content), 1)

    def test_recipe_category_status_code_200(self):
        self.make_recipe(category={'name': 'pao'})
        response = self.response_get_category()
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_status_code_404(self):
        response = self.response_get_category(category_id=999)
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_category_altered(self):
        self.make_recipe(category={'name': 'Especial'})
        response = self.response_get_category()
        response_content = response.context['recipes'].first()
        self.assertEqual(response_content.category.name, 'Especial')

    def test_recipe_category_template_has_data(self):
        self.make_recipe()
        response = self.response_get_category()
        content = response.content.decode('utf-8')
        self.assertIn('Nova Categoria', content)

    def test_category_show_404_if_not_published(self):
        self.make_recipe(is_published=False)
        response = self.response_get_category()
        assert response.status_code == 404