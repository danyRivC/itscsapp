from django.contrib import admin
from itscsapp.research.models import *


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ['title']
