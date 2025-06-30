from django.urls import path
from .views import *

urlpatterns = [
    path('room/<str:room_id>/book/', RoomBookingCreateView.as_view(), name='book_room'),
  
    path('bookings/', BookingListCreateView.as_view(), name='booking_list'),
    path('booking/<str:pk>/', BookingDetailUpdateView.as_view(), name='booking_detail'),     
    path('booking/<str:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),


]