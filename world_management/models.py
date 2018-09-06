from django.db import models

# Create your models here.
class President(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

class Country(models.Model):
  name = models.CharField(max_length=100)
  president = models.ForeignKey(President, on_delete=models.CASCADE)
  population = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
