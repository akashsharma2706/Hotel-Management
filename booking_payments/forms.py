from django import forms
from .models import Booking ,Payment


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'total_price']
        widgets = {
                'check_in': forms.DateInput(attrs={'type': 'date'}),
                'check_out': forms.DateInput(attrs={'type': 'date'}),
            }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_mode', 'payment_type', 'payment_status'] 
