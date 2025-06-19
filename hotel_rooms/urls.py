from django.urls import path
from .views import *

urlpatterns = [

    path('hotel/', HotelListCreateView.as_view(), name='hotel_list'),
    path('hotel/<str:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('hotel/<str:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),
    path('hotel/<str:hotel_id>/room/add/', RoomCreateView.as_view(), name='room_create'),
    path('room/<str:pk>/edit/', RoomUpdateView.as_view(), name='room_update'),
    path('room/<str:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    path('review/<str:hotel_id>/add_review/', ReviewCreateView.as_view(), name='add_review'),
    path('review/<str:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('review/<str:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),


]