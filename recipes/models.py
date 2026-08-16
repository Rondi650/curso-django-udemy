from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default="")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title


"""
CRIANDO USER NO DJANGO SHELL (exemplo)
>>> from django.contrib.auth.models import User
>>> User.objects.create_user(first_name='XPTO',last_name='C3PO', 
username='pqp_pra_la',password='jafsyuhasfyfas1524')
"""

'''
DUPLICANDO RECEITAS PELO SHELL
>>> import random
>>> r = Recipe.objects.all()
>>> r
>>> for i in r:
...     i.id = None  # Reseta o ID para forçar a criação de um novo registro
...     sufixo = random.randint(100, 999)  # Gera um número aleatório
...     i.slug = f"{i.slug}-{sufixo}"        # Concatena como string (ex: 'bolo-de-pote-482')
...     i.save()
'''


'''
RENOMEANDO SLUGS
>>> r = Recipe.objects.all()
>>> r
<QuerySet [<Recipe: Bolo de Pote>, <Recipe: Almondega Recheada>, <Recipe: Frango com Quiabo>...]

>>> for i in r: print(i.slug)
pao-de-lo 117
bolo-de-pote 118
almondega-maneira 119...

import re
>>> for x,i in enumerate(r): p = re.search(r'[a-z]+(?:-[a-z]+)*',i.slug); print(p.group())
pao-de-lo
bolo-de-pote
almondega-maneira...

>>> for x,i in enumerate(r): p = re.search(r'[a-z]+(?:-[a-z]+)*',i.slug); i.slug=f'{p.group()}-{x+1}'; i.save()
>>> r
pao-de-lo-1
bolo-de-pote-2
almondega-maneira-3...
'''


'''
DELETANDO IDS PELO SHELL
>>> for i in r:
...     if i.id >=8:
...             i.delete()
... 
(1, {'recipes.Recipe': 1})
(1, {'recipes.Recipe': 1})

>>> r = Recipe.objects.all()  # Força nova consulta no banco
>>> r
<QuerySet [<Recipe: Bolo de Pote>, <Recipe: Almondega Recheada>, <Recipe: Frango com Quiabo>, <Recipe: Bolo de chololate>, <Recipe: Pao de Lo>]>
>>> len(r)
5

'''
