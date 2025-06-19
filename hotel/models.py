from django.db import models
from user_auth.models import User

ROOM_TYPE = [
    ('standard', 'standard'),
    ('deluxe', 'deluxe'),
    ('suit', 'suit'),
    ('dormitory', 'dormitory'),  
]
FACILITY_CHOICES = (
    ('wifi', 'Wi-Fi'),
    ('pool', 'Swimming Pool'),
    ('gym', 'Gym'),
    ('parking', 'Parking'),
    ('ac', 'Air Conditioning'),
    ('laundry', 'Laundry Service'),
    ('restaurant', 'Restaurant'),
    ('bar', 'Bar'),
    ('spa', 'Spa'),
    ('pet_friendly', 'Pet Friendly'),
    ('kids_play_area', 'Kids Play Area'),
    ('game_room', 'Game Room'),
    ('meeting_room', 'Meeting Room'),
)

LOCATION_CHOICES = (
    ('dshala', 'Dharamshala'),
    ('mnali', 'Manali'),
    ('kullu', 'Kullu'),
    ('baijnath', 'Baijnath'),
    ('hmirpur', 'Hamirpur'),
    ('kangra', 'Kangra'),
    ('chamba', 'Chamba'),
    ('jwalaji', 'Jawalaji'),
    ('nadaun', 'Nadaun'),
    ('ranikhet', 'Ranikhet'),
    ('athankot', 'Pathankot'),
    ('gaggal', 'Gaggal'),
    ('shahpur', 'Shahpur'),
)

class Image(models.Model):
    image = models.ImageField(upload_to='media') 



class Hotel(models.Model):
    name = models.CharField(max_length=100)
    hotel_image = models.ManyToManyField(Image, blank=True) 
    address = models.CharField(max_length=255)
    rating = models.IntegerField()
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='Dharamshala') 
    facilities = models.CharField(max_length=50, choices=FACILITY_CHOICES, default='wifi') 
    

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True)
    room_number = models.CharField(max_length=10)  
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE, default="AC") 
    room_image = models.ImageField(upload_to='hotel/hotel_image') 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_booked = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews') 
    comment = models.CharField(max_length=255, blank=True) 
    star_rating = models. CharField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.star_rating
    

    
