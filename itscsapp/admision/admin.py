from django.contrib import admin
from .models.admision_carrer import AdmisionCarrer
from .models.admision_event import AdmisionEvent


@admin.register(AdmisionCarrer)
class AdmisionCarrerAdmin(admin.ModelAdmin):
    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'carrer']
    list_display = ['first_name', 'last_name', 'phone', 'email', 'carrer']
    list_filter = ['carrer']


@admin.register(AdmisionEvent)
class AdmisionEventrAdmin(admin.ModelAdmin):
    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'event']
    list_display = ['first_name', 'last_name', 'phone', 'email', 'event']
    list_filter = ['event']

