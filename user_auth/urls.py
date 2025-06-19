from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 



urlpatterns = [
    path('hotel/', base.as_view(), name='hotel'),   
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
     path('register/', RegisterView.as_view(), name='register'),

]