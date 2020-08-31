from django import forms
from homepage.models import Ticket


class TicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)



