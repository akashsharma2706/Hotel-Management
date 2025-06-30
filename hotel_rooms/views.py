from hotel_rooms.models import Hotel, Room, Review
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RoomForm, HotelForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin


class HotelListCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView, ListView):
    model = Hotel
    form_class= HotelForm
    context_object_name = 'hotels'
    template_name = 'hotel_list.html'
    object_list = Hotel.objects.all()
    success_url = reverse_lazy('hotel_list')
    success_message = "Hotel created successfully"

    def get_queryset(self):
        return super().get_queryset() 
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'manager':
            return Hotel.objects.for_user(user)
        else:
            return Hotel.objects.all()
       
    def get_initial(self):
        initial = super().get_initial()
        initial['manager'] = self.request.user
        return initial   


class HotelDetailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView, DetailView):
    model = Hotel
    context_object_name = 'hotel'
    template_name = 'hotel_detail.html'
    fields ='__all__'
    success_message = "Hotel updated successfully"

    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.object.pk})
    

class HotelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Hotel
    template_name = 'delete.html'
    success_url = reverse_lazy('hotel_list')
    success_message = "Hotel deleted successfully"


class RoomListCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_create.html'

    def form_valid(self, form):
        hotel = get_object_or_404(Hotel, id=self.kwargs['hotel_id'])
        form.instance.hotel = hotel
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hotel = get_object_or_404(Hotel, id=self.kwargs['hotel_id'])
        context['hotel'] = hotel
        return context
    
    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.object.hotel.pk})
    
    
class RoomDetailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView, DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'room_create.html'
    fields = '__all__'
    success_message = "Room updated successfully"
    
    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.object.hotel.pk})


class RoomDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Room
    template_name = 'delete.html'
    success_message = "Room deleted successfully"

    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.object.hotel.pk})
       

class ReviewListCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'room_create.html'

    def form_valid(self, form):
        hotel = get_object_or_404(Hotel, id=self.kwargs['hotel_id'])
        form.instance.hotel = hotel
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.kwargs['hotel_id']})
    

class ReviewDetailUpdateView(LoginRequiredMixin, DetailView, UpdateView):
    model = Review
    form_class = ReviewForm 
    template_name = 'room_create.html' 

    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.object.hotel.pk})
    

class ReviewDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Review
    template_name = 'delete.html'  
    success_message = "Review deleted successfully"

    def get_success_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.object.hotel.pk})
    


    
    

    

    









    
   



  


    
















