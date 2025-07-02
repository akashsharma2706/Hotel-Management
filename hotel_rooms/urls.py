from django.urls import path
from .views import *

urlpatterns = [

    path('hotel/', HotelListCreateView.as_view(), name='hotel_list'),
    path('hotel/<str:pk>/', HotelDetailUpdateView.as_view(), name='hotel_detail'),
    path('hotel/<str:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),

    path('hotel/<str:hotel_id>/roomadd/', RoomListCreateView.as_view(), name='room_create'),
    path('room/<str:pk>/edit/', RoomDetailUpdateView.as_view(), name='room_update'),
    path('room/<str:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),

    path('hotel/<str:hotel_id>/reviews/', ReviewListCreateView.as_view(), name='add_review'),
    path('review/<str:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('review/<str:pk>/edit/', ReviewDetailUpdateView.as_view(), name='review_update'),



]