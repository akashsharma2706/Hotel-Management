from django.urls import path
from .views import BookingListCreateView, BookingDetailUpdateView, BookingDeleteView

urlpatterns = [

    path('room/<str:room_id>/bookings/', BookingListCreateView.as_view(), name='booking_list_create'),
    path('booking/<str:pk>/', BookingDetailUpdateView.as_view(), name='booking_detail'),     
    path('booking/<str:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),


]