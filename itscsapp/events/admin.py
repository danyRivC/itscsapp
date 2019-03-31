from django.contrib import admin

from .models.event import EventModel


@admin.register(EventModel)
class EventAdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
