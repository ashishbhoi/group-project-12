from django.contrib import admin
from .models import (
    Course,
    Prerequisite,
    QuestionPaper
)


admin.site.register(Course)
admin.site.register(Prerequisite)
admin.site.register(QuestionPaper)
