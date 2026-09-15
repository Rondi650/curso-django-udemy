from django.shortcuts import render
from authors.forms import RegisterForm
from django.http import HttpRequest

# Create your views here.


def register_view(request: HttpRequest):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'author/pages/register_view.html', {
        'form': form,
    })