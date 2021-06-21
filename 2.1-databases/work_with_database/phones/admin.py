from django.contrib import admin

from .models import Phone


class Phones(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Phone, Phones)
