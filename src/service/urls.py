from django.urls import path, re_path, include
from django.contrib import admin

from service import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$',
        views.ItemDetailView.as_view(),
        name='item'
    ),
    path('', include('django_classified.urls')),
]
