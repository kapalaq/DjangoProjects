from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from django.conf import settings


# Create your views here.
def index(request):
    events = Event.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on').values()
    context = {
        'title': 'Ne Sxodim',
        'events': events,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/index.html', context=context)


def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'title': event.title,
        'diff': (event.seats_available - event.seats_taken),
        'event': event,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/event.html', context=context)


def faqs_contacts(request):
    context = {
        'title': "FAQs and Contacts",
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/faq.html', context=context)
