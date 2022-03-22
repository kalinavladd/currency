from django.urls import path

from .views import (SourceCreateViews,
                    SourceDeleteViews,
                    SourceListViews,
                    SourceUpdateViews,
                    contactus_list,
                    rate_views,)


urlpatterns = [
    path('', contactus_list),
    path('rate', rate_views),
    path('sources/', SourceListViews.as_view(), name='sources'),
    path('sources/create/', SourceCreateViews.as_view(), name='create_source'),
    path('sources/update/<int:pk>', SourceUpdateViews.as_view(), name='update_source'),
    path('sources/delete/<int:pk>', SourceDeleteViews.as_view(), name='delete_source'),
]
