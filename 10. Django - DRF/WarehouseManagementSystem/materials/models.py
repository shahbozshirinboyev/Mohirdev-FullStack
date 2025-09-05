from django.db import models

# Create your models here.
class Material(models.Model):
  material_name = models.CharField(max_length=100)
  unit = models.CharField(max_length=20)  # m², metr, dona

  def __str__(self):
    return f'{self.material_name}'
