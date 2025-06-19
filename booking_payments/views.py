from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Hotel, Booking, Payment
from .forms import BookingForm, PaymentForm

class RoomBookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'room_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.hotel = get_object_or_404(Hotel, id=self.kwargs['hotel_id'])
        self.room = get_object_or_404(self.hotel.room, id=self.kwargs['room_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['room'] = self.room
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.hotel = self.hotel
        form.instance.room = self.room
        response = super().form_valid(form)
        self.room.is_booked = False
        self.room.save()

        Payment.objects.create(
        booking=self.object,
        user=self.request.user,
        payment_status='paid',
        payment_mode='online'
)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel'] = self.hotel
        context['room'] = self.room
        return context

    def get_success_url(self):
        return reverse_lazy('hotel_detail', kwargs={'pk': str(self.hotel.id)})


class BookingListCreateView(LoginRequiredMixin, CreateView, ListView):
    model = Booking
    form_class= BookingForm
    context_object_name = 'bookings'
    template_name = 'booking_list.html'
    object_list = Hotel.objects.all()
    success_url = reverse_lazy('booking_list')

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'user_type') and user.user_type == 'manager':
            return Booking.objects.filter(hotel__manager=user)
        return Booking.objects.filter(user=user)


class BookingDetailView(LoginRequiredMixin, UpdateView, DetailView ):
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

    def get_success_url(self):
        return reverse_lazy('booking_detail', kwargs={'pk': self.object.pk})

    def get_success_url(self):
        booking = self.get_object()
        if booking:
            return reverse_lazy('booking_detail', kwargs={'pk': booking.id})
        return reverse_lazy('hotel_list')  
    
    
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking 
    template_name = 'delete.html'
    success_url = reverse_lazy('booking_list')

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'user_type') and user.user_type == 'manager':
            return Booking.objects.filter(hotel__manager=user)
        return Booking.objects.filter(user=user)
    


    
    
    

    
    



    
    
 

