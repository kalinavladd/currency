from django.urls import path


from .views import (ContactUsCreateView, ContactUsList,
                    RateDeleteView, RateListView, RateUpdateView,
                    SourceCreateViews, SourceDeleteViews, SourceListViews, SourceUpdateViews)


urlpatterns = [
    path('', ContactUsList.as_view(), name='contact_list'),
    path('create', ContactUsCreateView.as_view(), name='create_contact'),
    path('rate', RateListView.as_view(), name='rate'),
    path('rate/<int:pk>', RateUpdateView.as_view(), name='rate_update'),
    path('rate_delete/<int:pk>', RateDeleteView.as_view(), name='rate_delete'),
    path('sources/', SourceListViews.as_view(), name='sources'),
    path('sources/create/', SourceCreateViews.as_view(), name='create_source'),
    path('sources/update/<int:pk>', SourceUpdateViews.as_view(), name='update_source'),
    path('sources/delete/<int:pk>', SourceDeleteViews.as_view(), name='delete_source'),
]
