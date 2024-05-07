from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import login, views
from django.contrib.auth.decorators import login_required

from .models import Event, User, UserEvent, UserProfile
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
        temp = RegisterForm(None, 0, request.POST)
        if temp.is_valid():
            event.increase()
            user = get_object_or_404(UserProfile, user=request.user)
            user_event = UserEvent.objects.create(user=user, event=event, place=temp.cleaned_data['place'])
            user_event.save()
        else:
            print(temp.errors)

    form = RegisterForm(event=event, av=event.seats_available)
    context = {
        'title': event.title,
        'diff': (event.seats_available - event.seats_taken),
        'event': event,
        'user': request.user,
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


class CustomLoginView(views.LoginView):
    template_name = 'eventBlog/login.html'


@login_required
def my_page(request):
    user_events = UserEvent.objects.filter(user=get_object_or_404(UserProfile, user=request.user))
    context = {
        'title': 'My Page',
        'user': request.user,
        'user_events': user_events,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'eventBlog/account.html', context)
