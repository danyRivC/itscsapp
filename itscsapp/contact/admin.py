from django.contrib import admin
from itscsapp.contact.models.contact import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'phone_number']
    readonly_fields = ['name', 'subject', 'email', 'message', 'phone_number', 'created', 'updated' ]
