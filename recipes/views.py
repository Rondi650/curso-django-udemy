from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,
                  template_name='recipes/home.html',
                  context={'nome': 'Rondi Oliveira'},
                  status=202)


def temp(request):
    return render(request,
                  template_name='temp/temp.html',
                  context={'titulo': 'Teste Temporario'},
                  status=202)
