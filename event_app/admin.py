from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Organization, Event


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
