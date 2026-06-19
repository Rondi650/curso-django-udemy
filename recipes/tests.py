from django.test import TestCase
import pytest

# Create your tests here.


@pytest.mark.slow
class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        print('bom dia')
        assert 1 == 1, 'Um é igual a um'


class Test_erro(TestCase):
    def test_erro(self):
        assert 1 == 2
