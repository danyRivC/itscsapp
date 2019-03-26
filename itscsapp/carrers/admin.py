from django.contrib import admin
from itscsapp.carrers.models import *


@admin.register(Carrer)
class CarrerAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(InformationCarrer)
class InformationCarrerAdmin(admin.ModelAdmin):
    list_display = ['carrer']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_name']


@admin.register(Asignature)
class AsignatureAdmin(admin.ModelAdmin):
    list_display = ['name_assignature']
