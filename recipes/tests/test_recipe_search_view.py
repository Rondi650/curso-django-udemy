from recipes.tests.test_base import RecipeTestBase
from django.urls import resolve, reverse
from recipes import views


class RecipeSearchViewTest(RecipeTestBase):
    def test_recipe_search_uses_correct_view_function(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_search_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?search=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?search=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Resultados para: &lt;Teste&gt;',
            response.content.decode('utf-8')
        )

    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'
        
        recipe1 = self.make_recipe(
            slug = 'teste',
            title=title1,
            author={'username': 'rondi'}
        )
        
        recipe2 = self.make_recipe(
            slug = 'teste2',
            title=title2,
            author={'username': 'rondinelle'}
        )
        
        search_url = reverse('recipes:search')
        response1 = self.client.get(search_url  + f'?search={title1}') 
        response2 = self.client.get(search_url  + f'?search={title2}')
        response_both = self.client.get(search_url  + f'?search=this')
        
        print('*' * 50)
        print(response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])
