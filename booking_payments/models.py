from django.db import models
from hotel_rooms.models import Room, Hotel, BaseMixin
from user_auth.models import User
from .constants import PAY_MODE, PAY_STATUS, PAY_TYPE


class Booking(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    booking_mode = models.CharField(max_length=50, choices=PAY_MODE, blank=True, default='online')  

    def __str__(self): 
        return self.user.username
 
    
class Payment(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True, related_name='booking_payment')
    payment_mode = models.CharField(max_length=50, choices=PAY_MODE, blank=True, default='online')
    payment_type = models.CharField(max_length=50, choices=PAY_TYPE, blank=True, default='debit')
    payment_status = models.CharField(max_length=50, choices=PAY_STATUS, blank=True, default='unpaid')
    
    def __str__(self):
        return self.payment_status
