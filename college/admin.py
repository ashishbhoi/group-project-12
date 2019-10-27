from django.contrib import admin
from .models import (
    Classroom,
    Section
)

admin.site.register(Classroom)
admin.site.register(Section)
