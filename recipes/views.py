from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,
                  template_name='recipes/pages/home.html',
                  context={'nome': 'Rondi Oliveira'},
                  status=202)
