from django.db import models
from user_auth.models import User
import uuid
from django.db.models import Q, Avg, Count
from django.core.validators import MaxValueValidator

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


class BaseMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)
    
    class Meta:
        abstract = True

class Image(BaseMixin):
    image = models.ImageField(upload_to='media') 
    def __str__(self):
        return self.image.url
    

class Room(BaseMixin):
    room_number = models.CharField(max_length=10)  
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE, default="AC") 
    room_image = models.ManyToManyField(Image, blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_booked = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number
    
class HotelManager(models.Manager):
    def for_user(self, user):
        return self.filter(Q(manager=user)).distinct()
    
class Review(BaseMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    comment = models.CharField(max_length=255, blank=True) 
    star_rating = models. IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment

class Facilities(BaseMixin):
    facilities = models.CharField(max_length=50, choices=FACILITY_CHOICES, default='wifi')
    
    def __str__(self):
        return self.facilities

class Hotel(BaseMixin):
    room = models.ManyToManyField(Room, blank=True, related_name='hotel_room')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='hotel_manager')
    name = models.CharField(max_length=100)
    hotel_image = models.ImageField(upload_to='media')
    address = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='Dharamshala') 
    facilities = models.ManyToManyField(Facilities, blank=True, related_name='hotel_facilities')
    review = models.ManyToManyField(Review, blank=True, related_name='hotel_review') 


    objects = HotelManager()

    def average_rating(self):
        avg = self.review.aggregate(avg_rating=Avg('star_rating'))['avg_rating']
        return round(avg or 0, 1)

    def total_review(self):
        total_reviews_count = self.review.aggregate(reviews_count=Count('comment'))['reviews_count']
        return total_reviews_count




    def __str__(self):
        return self.name


    

    
