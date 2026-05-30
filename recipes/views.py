from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,
                  template_name='recipes/pages/home.html',
                  context={
                      'page_title': 'Home'
                  }
                  )

def recipe(request, id):
    return render(request,
                  template_name='recipes/pages/recipe-view.html',
                  context={
                      'page_title': 'Recipes'
                  }
                  )
