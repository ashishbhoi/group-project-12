from django.db import models
from department.models import Department
from college.models import Section


semester_select = [
    ('autumn', 'Autumn'),
    ('summer', 'Summer'),
    ('winter', 'Winter'),
    ('spring', 'Spring'),
]


class Instructor(models.Model):
    i_id = models.CharField(max_length=15, primary_key=True)
    login_password = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    dept_name = models.ForeignKey(Department, models.SET_NULL, null=True, db_column='dept_name')

    def __str__(self):
        return "%s (%s)" % (self.i_id, self.name)


class Teaches(models.Model):
    i_id = models.ForeignKey(Instructor, models.CASCADE, db_column='i_id')
    section = models.ForeignKey(Section, models.SET_NULL, null=True)

    class Meta:
        unique_together = (('i_id', 'section'),)


class Project(models.Model):
    project_id = models.CharField(max_length=20, primary_key=True)
    i_id = models.ForeignKey(Instructor, models.SET_NULL, null=True, db_column='i_id')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    semester = models.CharField(max_length=10, choices=semester_select)
    year = models.DecimalField(max_digits=4, decimal_places=0)

    def __str__(self):
        return "%s (%s)" % (self.project_id, self.title)
