from django.db import models
from django.template.defaultfilters import truncatechars


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=150, unique=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject

    @property
    def message_short_descriptions(self):
        return truncatechars(self.message, 50)


class Rate(models.Model):
    types = models.CharField(max_length=5)
    source = models.CharField(max_length=64)
    created = models.DateTimeField()
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
