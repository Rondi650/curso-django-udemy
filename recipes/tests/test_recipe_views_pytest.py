from django.urls import resolve, reverse
from recipes import views

def test_recipe_views_with_pytest():
    # apenas testando uso do pytest
    view_h = resolve(reverse('recipes:home'))
    view_c = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    view_r = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
    assert views.home is view_h.func
    assert views.category is view_c.func
    assert views.recipe is view_r.func
