from django.shortcuts import render, redirect

from .models import ContactUs, Rate, Source
from .forms import SourceForm

# Create your views here.


def contactus_list(requests):
    contactus = ContactUs.objects.all()
    return render(requests, "contact_table.html", context={"contactus": contactus})


def rate_views(requests):
    rate = Rate.objects.all()
    return render(requests, "rate.html", context={"rate": rate})


def source_views(request):
    sources = Source.objects.all()
    return render(request, 'sources.html', context={'sources': sources})


def create_source(request):
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sources')
    else:
        form = SourceForm()
    return render(request, 'source_create.html', context={'form': form})
