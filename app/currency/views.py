from django.shortcuts import render

from .models import ContactUs

# Create your views here.


def contactus_list(requests):
    contactus = ContactUs.objects.all()
    return render(requests, "contact_table.html", context={"contactus": contactus})
