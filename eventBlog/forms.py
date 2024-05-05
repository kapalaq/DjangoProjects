from django import forms
import random


class RegisterForm(forms.Form):
    place = forms.IntegerField(widget=forms.Select(choices=[]), label="Place")
    credit_card = forms.IntegerField(max_value=9999999999999999, min_value=1000000000000000, label="Credit Card")

    def __init__(self, av=0, tk=0, *args, **kwargs):
        choices = set()
        while len(choices) < (av - tk):
            n = random.randint(1, av)
            choices.add((n, n))
        super().__init__(*args, **kwargs)
        self.fields["place"].widget.choices = sorted(choices)
