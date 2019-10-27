from django.db import models
from student.models import Student
from course.models import Course

class Specialization(models.Model):
    spec_id = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=15)

    def __str__(self):
        return "%s (%s)" % (self.spec_id, self.title)

class Survey(models.Model):
    roll_number = models.ForeignKey(Student, models.CASCADE, db_column='roll_number')
    course_id = models.ForeignKey(Course, models.CASCADE, db_column='course_id')
    spec_id = models.ForeignKey(Specialization, models.CASCADE, db_column='spec_id')    

    class Meta:
        unique_together = (('roll_number', 'course_id', 'spec_id'),)

