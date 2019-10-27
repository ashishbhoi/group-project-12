from django.contrib import admin
from .models import (
    Student,
    Takes,
    TakesProject
)


admin.site.register(Student)
admin.site.register(Takes)
admin.site.register(TakesProject)
