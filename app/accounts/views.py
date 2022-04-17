from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView


from .models import User
# Create your views here.


class MyProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'my_profile.html'
    success_url = reverse_lazy('sources')
    fields = (
        'first_name',
        'last_name',
    )

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            queryset = queryset.filter(id=self.request.user.id)
            return queryset
