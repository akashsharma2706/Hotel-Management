from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 



urlpatterns = [
    path('hotel/', HotelListView.as_view(), name='hotel'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('manager/', ManagerView.as_view(), name='manager'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path("register/", RegistrationView.as_view(), name="register"),

]