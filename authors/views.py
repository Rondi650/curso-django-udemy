from django.shortcuts import render
from authors.forms import RegisterForm

# Create your views here.


def register_view(request):
    form = RegisterForm()
    return render(request,
                  template_name='author/pages/register_view.html',
                  context={
                      'form': form
                  })
