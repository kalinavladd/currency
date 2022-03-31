from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from .forms import SourceForm
from .models import ContactUs, Rate, Source

# Create your views here.


class ContactUsList(ListView):
    model = ContactUs
    template_name = 'contact_table.html'
    context_object_name = 'contactus'


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('contact_list')
    fields = (
        'email_from',
        'subject',
        'message',
    )

    def _send_email(self):
        recipient = settings.EMAIL_HOST_USER
        subject = 'User ContactUS'
        body = f'Request From: {self.object.email_from}'
        send_mail(subject, body, recipient, [recipient], fail_silently=False)

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


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
