from django.db import models
from department.models import Department

semester_select = [
    ('autumn', 'Autumn'),
    ('summer', 'Summer'),
    ('winter', 'Winter'),
    ('spring', 'Spring'),
]


class Course(models.Model):
    course_id = models.CharField(max_length=6, primary_key=True)
    course_name = models.CharField(max_length=100)
    dept_name = models.ForeignKey(Department, models.SET_NULL, null=True, db_column='department')
    credit = models.DecimalField(max_digits=2, decimal_places=0)
    new_performance = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (self.course_id, self.course_name)
    

class Prerequisite(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, related_name='course1')
    prereq = models.ForeignKey(Course, models.SET_NULL, null=True, related_name='course2')
    
    class Meta:
        unique_together = (('course', 'prereq'),)

    def __str__(self):
        return "%s --> %s" % (self.course, self.prereq)
    

class QuestionPaper(models.Model):
    course_id = models.ForeignKey(Course, models.CASCADE, db_column='course_id')
    exam_name = models.CharField(max_length=10)
    semester = models.CharField(max_length=10, choices=semester_select)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    path = models.URLField()

    class Meta:
        unique_together = (('course_id', 'exam_name', 'semester', 'year'),)
