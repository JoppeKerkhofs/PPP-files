from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(default='static/food/default.svg', blank=True, upload_to='static/food')

    def __str__(self):
        return self.name
