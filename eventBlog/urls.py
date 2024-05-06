from django.urls import path
from .views import *

urlpatterns = [
    path('', view=index, name='main'),
    path('event/<int:event_id>', view=event_details, name='details'),
    path('FAQsAndContacts', view=faqs_contacts, name='faqs and contacts'),
    path('registration', view=registration_page, name='registration'),
    path('login', view=CustomLoginView.as_view(), name='login'),
    path('account', view=my_page, name='my page')
]
