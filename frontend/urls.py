from django.urls import path

from .views import detail_view


urlpatterns = [
    path("<str:uuid>/detail", detail_view, name="offender-detail"),
]
