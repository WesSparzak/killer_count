from django.db import models

# Create your models here.

from django.db import models

class Killer(models.Model):
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name
