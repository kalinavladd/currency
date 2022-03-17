from django.contrib import admin

from .models import ContactUs, Rate


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email_from', 'message_short_descriptions',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'buy',)
