
from django.contrib import admin
from App.models import Event

#admin.site.register(Student)

class EventAdmin(admin.ModelAdmin):
    list_display = ['username', 'EventName', 'Email', 'EventDate', 'phone_number', 'Alt_Phone_number',
                    'Effordable_Amount', 'Description'];
admin.site.register(Event,EventAdmin);