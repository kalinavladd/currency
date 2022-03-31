from django.urls import path

from .views import (ContactUsCreateView, ContactUsList, SourceCreateViews, SourceDeleteViews, SourceListViews,
                    SourceUpdateViews,
                    rate_views)


urlpatterns = [
    path('', ContactUsList.as_view(), name='contact_list'),
    path('create', ContactUsCreateView.as_view(), name='create_contact'),
    path('rate', rate_views),
    path('sources/', SourceListViews.as_view(), name='sources'),
    path('sources/create/', SourceCreateViews.as_view(), name='create_source'),
    path('sources/update/<int:pk>', SourceUpdateViews.as_view(), name='update_source'),
    path('sources/delete/<int:pk>', SourceDeleteViews.as_view(), name='delete_source'),
]
