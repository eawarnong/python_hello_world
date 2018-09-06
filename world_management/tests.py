from django.test import TestCase
from world_management.models import President, Country

# Create your tests here.
class PresidentTestCase(TestCase):
  def setUp(self):
    President.objects.create(first_name="John", last_name="Doe")
  
  def test_president_model(self):
    president_models = President.objects.count()
    self.assertEqual(president_models, 1)

class CountryTestCase(TestCase):
  def setUp(self):
    Country.objects.create(
      name="bkk",
      president=President.objects.create(first_name="John", last_name="Doe"),
      population=0,
    )

  def test_country_model(self):
    country_models = Country.objects.count()
    self.assertEqual(country_models, 1)