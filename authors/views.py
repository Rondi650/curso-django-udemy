from django.shortcuts import render

# Create your views here.


def register_view(request):
    return render(request,
                  template_name='author/pages/register_view.html')
