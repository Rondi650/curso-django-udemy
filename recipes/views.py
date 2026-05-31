from django.shortcuts import render
from utils._faker import make_recipe

# Create your views here.


def home(request):
    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': 'Home',
                      'recipes': [make_recipe() for _ in range(10)]
                  }
                  )


def recipe(request, id):
    return render(request,
                  template_name='recipes/pages/recipe-view.html',
                  context={
                      'page_title': 'Recipes',
                      'recipe': make_recipe(),
                      'is_detail_page': True
                  }
                  )
