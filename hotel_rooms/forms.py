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
        fields = ['room_number', 'room_type', 'room_image', 'price', 'is_booked']
        


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star_rating', 'comment'] 




