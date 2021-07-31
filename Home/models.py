from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField();

    def __str__(self):
        return self.title

class data(models.Model):
    name=models.CharField(max_length=200)
    continent=models.CharField(max_length=100)
    expense=models.CharField(max_length=100)
    deadline=models.DateField()

    def __str__(self):
        return self.name+self.continent