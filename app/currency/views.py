from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import SourceForm
from .models import ContactUs, Rate, Source
# Create your views here.


def contactus_list(requests):
    contactus = ContactUs.objects.all()
    return render(requests, "contact_table.html", context={"contactus": contactus})


def rate_views(requests):
    rate = Rate.objects.all()
    return render(requests, "rate.html", context={"rate": rate})


class SourceListViews(ListView):
    queryset = Source.objects.all().order_by('-id')
    template_name = 'sources.html'


class SourceCreateViews(CreateView):
    model = Source
    template_name = "source_create.html"
    form_class = SourceForm
    success_url = reverse_lazy('sources')


class SourceUpdateViews(UpdateView):
    model = Source
    template_name = "source_update.html"
    form_class = SourceForm
    success_url = reverse_lazy('sources')


class SourceDeleteViews(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('sources')
