from django.contrib import admin
from django.urls import path, include
from recipes.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
