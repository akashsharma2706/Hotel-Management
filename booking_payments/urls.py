# urls.py
from django.urls import path
from .views import RoomBookingCreateView, BookingListCreateView, BookingDetailView, BookingDeleteView

urlpatterns = [
    path('hotel/<uuid:hotel_id>/room/<uuid:room_id>/book/', RoomBookingCreateView.as_view(), name='book_room'),
    path('bookings/', BookingListCreateView.as_view(), name='booking_list'),
    path('booking/<str:pk>/', BookingDetailView.as_view(), name='booking_detail'),     
    path('booking/<str:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),

    # Add your hotel_detail path as needed

    
]
