from django import forms
from .models import Hotel, Room, Review
from booking_payments.models import Booking
 
class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"
       

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star_rating', 'comment'] 




