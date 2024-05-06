from django.conf import settings
from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField

from django.contrib.auth.models import User


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField(verbose_name="price (KZT)")
    date = models.DateTimeField(blank=True, null=True)
    time = models.TimeField(null=True, blank=True)
    created_on = models.DateTimeField(blank=True)
    posted_on = models.DateTimeField(null=True, blank=True)
    poster = models.ImageField(upload_to='image', null=True, blank=True)
    resized_poster = ResizedImageField(size=[640, 360], crop=['middle', 'center'], upload_to='resized_image',
                                       null=True, blank=True, verbose_name="Resized Poster (16:9 only)")
    place = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=24, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    seats_available = models.IntegerField(verbose_name="Number of seats available", default=0)
    seats_taken = models.IntegerField(verbose_name="Number of seats taken", default=0)

    def publish(self):
        self.posted_on = timezone.now()
        self.resized_poster = self.poster
        self.save()

    def increase(self):
        self.seats_taken += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Events"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)

    def is_registered(self):
        return self.registered

    class Meta:
        verbose_name_plural = "User Profiles"
