from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView
from .forms import RegistrationForm
from . models import Hotel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView


class base(TemplateView):
    template_name = 'base.html'  


class HotelListView(LoginRequiredMixin, ListView,):
    model = Hotel
    template_name = 'hotel_list.html'  
    context_object_name = 'hotels'  
    paginate_by = 10 


class CustomerView(LoginRequiredMixin, ListView,):
    model = Hotel
    template_name = 'customer_view.html'  
    context_object_name = 'hotels'  
    paginate_by = 10 

class ManagerView(LoginRequiredMixin, ListView,):
    model = Hotel
    template_name = 'manager_view.html'  
    context_object_name = 'hotels'  
    paginate_by = 10 

    

# User_authentication
class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
 
    def get_success_url(self):
        return reverse_lazy('hotel') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')