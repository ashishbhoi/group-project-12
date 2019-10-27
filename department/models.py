from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=8, primary_key=True)
    building = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.department
    