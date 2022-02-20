import random
import string

from django.http import HttpResponse

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
