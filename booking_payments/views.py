from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from .models import Booking, Room
from .forms import BookingForm, PaymentForm
from django.contrib.messages.views import SuccessMessageMixin


class BookingListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView, CreateView):
    template_name = 'booking_list.html'
    form_class = BookingForm
    success_message = 'Your room is booked'
    
    def get(self, request, room_id, *args, **kwargs):
        user = request.user
        if hasattr(user, 'user_type') and user.user_type == 'manager':
            bookings = Booking.objects.filter(room__hotel__manager=user)
        else:
            bookings = Booking.objects.filter(user=user)
        form = self.form_class()
        return render(request, self.template_name, {'bookings': bookings, 'form': form})

    def post(self, request, room_id, *args, **kwargs):
        form = self.form_class(request.POST)
        user = request.user
        if hasattr(user, 'user_type') and user.user_type == 'manager':
            bookings = Booking.objects.filter(room__hotel__manager=user)
        else:
            bookings = Booking.objects.filter(user=user)
        if form.is_valid():
            room = get_object_or_404(Room, id=room_id)
            form.instance.user = user
            form.instance.room = room
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            conflict = Booking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exists()
            if conflict:
                form.add_error(None, "This room is already booked for the selected dates.")
                return self.form_invalid(form)
            return super().form_valid(form)

    def get_success_url(self):
            return reverse('hotel_detail', kwargs={'pk': self.object.room.hotel.pk})
   
    
class BookingDetailUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView, DetailView ):
    model = Booking
    form_class= BookingForm        
    context_object_name = 'booking_detail'
    template_name = 'booking_detail.html'
    success_message = "booking updated successfully"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_form'] = PaymentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.user = request.user
            payment.booking = self.object
            payment.save()

            return redirect('booking_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

    
class BookingDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Booking 
    template_name = 'delete.html'
    success_message = "booking deleted successfully"

    def get_success_url(self):
            return reverse('booking_list_create', kwargs={'room_id': self.object.room_id})




    


    
    
    

    
    



    
    
 

