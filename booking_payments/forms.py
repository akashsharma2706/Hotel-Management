# forms.py
from django import forms
from .models import Booking ,Payment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'total_price']

    def __init__(self, *args, **kwargs):
        self.room = kwargs.pop('room', None)
        super().__init__(*args, **kwargs)

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_mode', 'payment_type', 'payment_status'] 
