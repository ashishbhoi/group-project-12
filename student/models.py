from django.db import models
from department.models import Department
from college.models import Section
from instructor.models import Project


class Student(models.Model):
    roll_number = models.CharField(max_length=15, primary_key=True)
    login_password = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    dept_name = models.ForeignKey(Department, models.SET_NULL, null=True, db_column='department')
    cpi = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    batch = models.CharField(max_length=15)

    def __str__(self):
        return "%s (%s)" % (self.roll_number, self.name)


class Takes(models.Model):
    roll_number = models.ForeignKey(Student, models.CASCADE, db_column='roll_number')
    section = models.ForeignKey(Section, models.SET_NULL, null=True)
    feedback = models.TextField(max_length=500, null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = (('roll_number', 'section'),)


class TakesProject(models.Model):
    project_id = models.ForeignKey(Project, models.CASCADE, db_column='project_id')
    roll_number = models.ForeignKey(Student, models.CASCADE, db_column='roll_number')
    performance = models.CharField(max_length=15, null=True, blank=True)
    feedback = models.TextField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = (('project_id', 'roll_number'),)
