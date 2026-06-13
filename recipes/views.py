from django.shortcuts import render
from utils._faker import make_recipe
from recipes.models import Recipe

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
    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': recipes.first().category.name,  # type: ignore
                      'recipes': recipes
                  }
                  )


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id, is_published=True).first()
    return render(request,
                  template_name='recipes/pages/recipe-view.html',
                  context={
                      'page_title': recipe.title,  # type: ignore
                      'recipe': recipe,
                      'is_detail_page': True
                  }
                  )
