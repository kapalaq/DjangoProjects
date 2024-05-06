from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import login, authenticate

from .models import Event
from .forms import RegisterForm, UserRegistrationForm


# Create your views here.
def index(request):
    events = Event.objects.filter(posted_on__lte=timezone.now()).order_by('-posted_on').values()
    context = {
        'title': 'Ne Sxodim',
        'events': events,
        'user': request.user,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/index.html', context=context)


def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        # doesn't work, made of random
        temp = RegisterForm(0, 0, request.POST)
        if temp.is_valid():
            # add reserved
            event.increase()
    form = RegisterForm(av=event.seats_available, tk=event.seats_taken)
    context = {
        'title': event.title,
        'diff': (event.seats_available - event.seats_taken),
        'event': event,
        'form': form,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/event.html', context=context)


def faqs_contacts(request):
    context = {
        'title': 'FAQs and Contacts',
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/faq.html', context=context)


def registration_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return index(request)
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Registration',
        'form': form,
    }
    return render(request, 'eventBlog/registration.html', context)


def my_page(request):
    pass
