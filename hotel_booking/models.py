from django.db import models
from hotel.models import Room, Hotel, Location
from user_auth.models import User

PAY_MODE = [
    ('online', 'Online'),
    ('offline', 'Offline'),
]

PAY_TYPE = [
    ('debit', 'Debit Card'),
    ('credit', 'Credit Card'),
    ('upi', 'UPI'),
    ('none', 'None'),
]

PAY_STATUS = [
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
    ('canceled', 'Canceled'),
]


class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True,)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    booking_mode = models.CharField(max_length=50, choices=PAY_MODE, blank=True, default='online')  
    def __str__(self):
        return self.guest.username
    
class Payment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True)
    payment_mode = models.CharField(max_length=50, choices=PAY_MODE, blank=True, default='online')
    payment_type = models.CharField(max_length=50, choices=PAY_TYPE, blank=True, default='debit')
    payment_status = models.CharField(max_length=50, choices=PAY_STATUS, blank=True, default='unpaid')

    def __str__(self):
        return self.payment_status
