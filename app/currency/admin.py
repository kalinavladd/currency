from currency.models import ContactUs, Rate, Source

from django.contrib import admin


@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_display = ('name', 'created', 'reply_to', 'subject')
    readonly_fields = ('created', 'name', 'reply_to', 'subject', 'body', 'raw_content')  # second variant

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate)
admin.site.register(Source)
