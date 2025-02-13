# tickets/forms.py

from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['worker', 'issue']
        widgets = {
            'worker': forms.Select(attrs={'class': 'form-control'}),
            'issue': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
