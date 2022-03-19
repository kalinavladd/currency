from django.contrib import admin

from .models import ContactUs, Rate, Source


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email_from', 'message_short_descriptions',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'buy',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_url', 'name',)
