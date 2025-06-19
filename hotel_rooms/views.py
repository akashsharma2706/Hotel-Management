from hotel_rooms.models import Hotel, Room, Review
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RoomForm, HotelForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect


class HotelListCreateView(LoginRequiredMixin, CreateView, ListView):
    model = Hotel
    form_class= HotelForm
    context_object_name = 'hotels'
    template_name = 'hotel_list.html'
    object_list = Hotel.objects.all()
    success_url = reverse_lazy('hotel_list')

    def get_queryset(self):
        print('>>>>> working ')
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


class HotelDetailView(LoginRequiredMixin, UpdateView, DetailView):
    model = Hotel
    context_object_name = 'hotel'
    template_name = 'hotel_detail.html'
    fields ='__all__'
    success_url = reverse_lazy('hotel_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.review.all().order_by('-date')
        context['review_form'] = ReviewForm()
        return context


class HotelDeleteView(LoginRequiredMixin, DeleteView):
    model = Hotel
    template_name = 'delete.html'
    success_url = reverse_lazy('hotel_list')


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'room_create.html'

    def form_valid(self, form):
        room = form.save()
        hotel_id = self.kwargs.get('hotel_id')
        hotel = get_object_or_404(Hotel, id=hotel_id)
        hotel.room.add(room)  # Add the room to the hotel's ManyToMany
        return redirect('hotel_detail', pk=hotel.id)
    
    


class RoomUpdateView(LoginRequiredMixin, UpdateView, DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'room_create.html'
    fields = '__all__'

    def get_success_url(self):
        # Get the first hotel associated with this room
        hotel = self.object.hotel_room.first()
        if hotel:
            return reverse('hotel_detail', kwargs={'pk': str(hotel.pk)})
        else:
            # Fallback: redirect to hotel list if no hotel is associated
            return reverse('hotel_list')


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'delete.html'

    def get_success_url(self):
        # Get the first hotel associated with this room BEFORE deletion
        hotel = self.object.hotel_room.first()
        if hotel:
            return reverse('hotel_detail', kwargs={'pk': str(hotel.pk)})
        else:
            # Fallback: redirect to hotel list if no hotel is associated
            return reverse('hotel_list')
        

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'room_create.html'  # Not used if you post from hotel_detail.html

    def dispatch(self, request, *args, **kwargs):
        self.hotel = get_object_or_404(Hotel, id=self.kwargs['hotel_id'])
        # Prevent duplicate review by the same user for this hotel
        if self.hotel.review.filter(user=request.user).exists():
            return redirect('hotel_detail', pk=self.hotel.id)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        review = form.save()
        self.hotel.review.add(review)
        return redirect('hotel_detail', pk=self.hotel.id)

    def get_success_url(self):
        return reverse_lazy('hotel_detail', kwargs={'pk': self.hotel.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = self.hotel
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user   # This sets the user to the logged-in user
        review = form.save()
        self.hotel.review.add(review)
        return redirect('hotel_detail', pk=self.hotel.id)
    

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm 
    template_name = 'room_create.html'  # Create this template

    

    def test_func(self):
        # Only allow the user who wrote the review to edit it
        review = self.get_object()
        return review.user == self.request.user

    def get_success_url(self):
        # Redirect to the hotel detail page after updating the review
        hotel = self.get_object().hotel_review.first()  # 'hotel_review' is the related_name
        if hotel:
            return reverse_lazy('hotel_detail', kwargs={'pk': hotel.id})
        return reverse_lazy('hotel_list')
    

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'delete.html'  # Create this template

    def test_func(self):
        # Only allow the user who wrote the review to delete it
        review = self.get_object()
        return review.user == self.request.user

    def get_success_url(self):
        # Redirect to the hotel detail page after deletion
        # Since it's ManyToMany, get the first hotel associated with this review
        hotel = self.get_object().hotel_review.first()  # 'hotel_review' is the related_name
        if hotel:
            return reverse_lazy('hotel_detail', kwargs={'pk': hotel.id})
        return reverse_lazy('hotel_list')  # fallback if no hotel found
    


    







    









    
   



  


    
















