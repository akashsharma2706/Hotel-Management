from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Hotel, Booking, Room
from .forms import BookingForm, PaymentForm


class RoomBookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'room_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        room_id = self.kwargs.get('room_id')
        room = get_object_or_404(Room, id=room_id)
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


class BookingListCreateView(LoginRequiredMixin, ListView):
    model = Booking
    context_object_name = 'bookings'
    template_name = 'booking_list.html'

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'user_type') and user.user_type == 'manager':
            return Booking.objects.filter(room__hotel__manager=user)
   
    
class BookingDetailUpdateView(LoginRequiredMixin, UpdateView, DetailView ):
    model = Booking
    form_class= BookingForm        
    context_object_name = 'booking_detail'
    template_name = 'booking_detail.html'

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

    
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking 
    template_name = 'delete.html'
    success_url = reverse_lazy('booking_list')



    


    
    
    

    
    



    
    
 

