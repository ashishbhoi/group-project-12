from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=20, primary_key=True)
    building = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.department
    