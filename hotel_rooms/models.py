from django.db import models
from user_auth.models import User
import uuid
from django.db.models import Q, Avg, Count
from django.core.validators import MaxValueValidator
from .constants import ROOM_TYPE, FACILITY_CHOICES, LOCATION_CHOICES


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

  
class HotelManager(models.Manager):
    def for_user(self, user):
        return self.filter(Q(manager=user)).distinct()
 

class Facilities(BaseMixin):
    facilities = models.CharField(max_length=50, choices=FACILITY_CHOICES, default='wifi')
    
    def __str__(self):
        return self.facilities


class Hotel(BaseMixin):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='hotel_manager')
    name = models.CharField(max_length=100)
    hotel_image = models.ImageField(upload_to='media')
    address = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='Dharamshala') 
    facilities = models.ManyToManyField(Facilities, blank=True, related_name='hotel_facilities')
    objects = HotelManager()

    def average_rating(self):
        avg = self.review.aggregate(avg_rating=Avg('star_rating'))['avg_rating']
        return round(avg or 0, 1)

    def total_review(self):
        total_reviews_count = self.review.aggregate(reviews_count=Count('comment'))['reviews_count']
        return total_reviews_count

    def __str__(self):
        return self.name


class Review(BaseMixin):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null= True, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    comment = models.CharField(max_length=255, blank=True) 
    star_rating = models.IntegerField(null=True, validators=[MaxValueValidator(5)])
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class Room(BaseMixin):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True ,null=True, related_name='hotel_rooms')
    room_number = models.CharField(max_length=10)  
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE, default="AC") 
    room_image = models.ManyToManyField(Image, blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_booked = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number


    

    
 