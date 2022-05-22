from django.db import models
from django.templatetags.static import static
from . import custom_choices as cmc


def logo_upload_to(instance, filename):
    return f'logo/{instance.name}/{filename}'


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    type = models.PositiveSmallIntegerField(    # noqa = A003
        choices=cmc.RateTypeChoices.choices,
        default=cmc.RateTypeChoices.USD,
        null=True
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE)


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    raw_content = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True)
    logo = models.FileField(
            upload_to=logo_upload_to,
            default=None,
            null=True,
            blank=True
        )

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return static('static/avatar.png')

    def __str__(self):
        return self.name
