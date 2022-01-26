from django.urls import path
from .views import OffenderView


urlpatterns = [
    path('upload/', OffenderView.as_view(), name='offender'),
]