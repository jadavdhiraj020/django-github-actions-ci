from django.test import TestCase
from .views import add



class MathTest(TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
