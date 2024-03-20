from django.contrib import admin
from django.utils.html import format_html

from .models import Organization, Event


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'postcode']
    list_filter = ['title', 'address', 'postcode']
    search_fields = ['title', 'address', 'postcode']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['title', 'date']
    search_fields = ['title', 'description', 'date']

    readonly_fields = ('preview_image', )
    fields = ['preview_image', 'image', 'title', 'description', 'date']

    def preview_image(self, model):
        return format_html(
            '<img src={} height={}/>',
            model.image.url,
            '200px'
        )
