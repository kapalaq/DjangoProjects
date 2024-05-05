from django.urls import path
from .views import *

urlpatterns = [
    path('', view=index, name='main'),
    path('event/<int:event_id>', view=event_details, name='details'),
    path('FaqsAndContacts', view=faqs_contacts, name='faqs and contacts'),
]
