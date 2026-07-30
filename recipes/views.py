from django.shortcuts import render
from utils._faker import make_recipe
from recipes.models import Recipe
from django.http import Http404

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': 'Home',
                      'recipes': recipes
                  }
                  )


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404

    category_name = recipes.first().category.name  # type: ignore

    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': f'{category_name} | Categoria',
                      'recipes': recipes
                  }
                  )


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id, is_published=True).first()

    if not recipe:
        raise Http404

    recipe_name = recipe.title  # type: ignore

    return render(request,
                  template_name='recipes/pages/recipe-view.html',
                  context={
                      'page_title': f'{recipe_name} | Receita',
                      'recipe': recipe,
                      'is_detail_page': True
                  }
                  )


def search(request):
    return render(request,
                  template_name='recipes/pages/search.html',)
