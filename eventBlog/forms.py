from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(forms.Form):
    place = forms.IntegerField(widget=forms.Select(choices=[]), label="Place")
    credit_card = forms.IntegerField(max_value=9999999999999999, min_value=1000000000000000, label="Credit Card")

    def __init__(self, event=None, av=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not (event is None and av == 0):
            choices = [(i, i) for i in range(1, av + 1)]
            self.fields["place"].widget.choices = choices
        else:
            choices = [(i, i) for i in range(1, 3)]
            self.fields["place"].widget.choices = choices


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'email',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'password',
                'required': True,
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'repeat password',
                'required': True,
            })
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
            profile = UserProfile.objects.create(user=user, registered=True)
            profile.save()
        return user
