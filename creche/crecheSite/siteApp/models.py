from django.db import models


# Create your models here.


class Employees(models.Model):
    website = models.URLField(blank=True)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname
