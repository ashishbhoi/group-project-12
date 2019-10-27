from django.contrib import admin
from .models import (
    Instructor,
    Teaches,
    Project,
)


admin.site.register(Instructor)
admin.site.register(Teaches)
admin.site.register(Project)
