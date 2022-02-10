from django.db import models
import uuid

from django.urls import reverse

# Create your models here.


class OffenderProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    speed = models.IntegerField(default=0)
    is_speeding = models.BooleanField(default=False)
    image = models.ImageField(upload_to='offenders/images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return (self.id)
    
    def get_absolute_url(self):
        return reverse("offender-detail", args=[str(self.id)])
