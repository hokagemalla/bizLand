from django.db import models


class Employees(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.TextField()
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname