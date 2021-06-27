from django.contrib import admin

from .models import Project, Measurement


admin.site.register(Project)
admin.site.register(Measurement)
