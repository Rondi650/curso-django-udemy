from django.contrib import admin
from django.urls import path
from recipes.views import home, temp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('temp/', temp),
]
