import random
import string

from django.http import HttpResponse
from .models import ContactUs

# Create your views here.


def gen_pass(pass_lenght: int = 10) -> str:
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''

    for _ in range(pass_lenght):
        password += random.choice(chars)
    return password


def hello_world(request):
    lenght = int(request.GET['lenght'])
    return HttpResponse(gen_pass(lenght))


def contact_us_view(request):
    contacts = []
    for line in ContactUs.objects.all():
        contacts.append([line.email_from, line.subject, line.message])
    return HttpResponse(contacts)
