from django.contrib import admin
from .models import (
    Specialization,
    Survey,
)


admin.site.register(Specialization)
admin.site.register(Survey)
