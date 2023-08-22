from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'event_date']


admin.site.register(Event, EventAdmin)