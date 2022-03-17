from django.shortcuts import render

from .models import ContactUs, Rate

# Create your views here.


def contactus_list(requests):
    contactus = ContactUs.objects.all()
    return render(requests, "contact_table.html", context={"contactus": contactus})


def rate_views(requests):
    rate = Rate.objects.all()
    return render(requests, "rate.html", context={"rate": rate})
