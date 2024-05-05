from django.conf import settings
from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField


class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField(verbose_name="price (KZT)")
    date = models.DateTimeField(blank=True, null=True)
    time = models.TimeField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now())
    posted_on = models.DateTimeField(null=True, blank=True)
    poster = ResizedImageField(size=[640, 360], crop=['middle', 'center'], upload_to='image', null=True, blank=True)
    place = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=24, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)

    def publish(self):
        self.posted_on = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Events"