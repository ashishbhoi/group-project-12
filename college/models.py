from django.db import models
from course.models import Course

semester_select = [
    ('autumn', 'Autumn'),
    ('summer', 'Summer'),
    ('winter', 'Winter'),
    ('spring', 'Spring'),
]


class Classroom(models.Model):
    building = models.CharField(max_length=15)
    room_no = models.CharField(max_length=8)
    capacity = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)

    class Meta:
        unique_together = (('building', 'room_no'),)
    
class Section(models.Model):
    course_id = models.ForeignKey(Course, models.CASCADE, db_column='course_id')
    sec_id = models.CharField(max_length=10)
    semester = models.CharField(max_length=8, choices=semester_select)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    building = models.ForeignKey(Classroom, models.SET_NULL, db_column='building', null=True, related_name='classroom1')
    room_no = models.ForeignKey(Classroom, models.SET_NULL, db_column='room_no', null=True, related_name='classroom2')

    class Meta:
        unique_together = (('course_id', 'sec_id', 'semester', 'year'),)
