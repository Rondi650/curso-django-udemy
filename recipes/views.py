from django.shortcuts import render
from django.db.models import Q
from recipes.models import Recipe
from django.http import Http404, HttpRequest
from django.core.paginator import Paginator
from utils.pagination import make_pagination

# Create your views here.

PER_PAGES = 9

def home(request: HttpRequest):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': 'Home',
                      'recipes': page_obj,
                      'pagination_range': pagination_range,
                  }
                  )


def category(request: HttpRequest, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404

    category_name = recipes.first().category.name  # type: ignore

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': f'{category_name} | Categoria',
                      'recipes': page_obj,
                      'pagination_range': pagination_range,
                  }
                  )


def recipe(request: HttpRequest, id):
    recipe = Recipe.objects.filter(id=id, is_published=True).first()

    if not recipe:
        raise Http404

    recipe_name = recipe.title  # type: ignore

    return render(request,
                  template_name='recipes/pages/recipe-view.html',
                  context={
                      'page_title': f'{recipe_name} | Receita',
                      'recipe': recipe,
                      'is_detail_page': True,
                  }
                  )


def search(request: HttpRequest):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        ),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGES)

    return render(request,
                  template_name='recipes/pages/search.html',
                  context={
                      'page_title': f'{search_term} | Pesquisa',
                      'search_term': search_term,
                      'recipes': page_obj,
                      'pagination_range': pagination_range,
                  }
                  )
