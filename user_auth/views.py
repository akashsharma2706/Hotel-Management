from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import User
from .forms import SignUpForm



class base(TemplateView):
    template_name = 'base.html'  
  

# User_authentication
class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
 
    def get_success_url(self):
        return reverse_lazy('hotel_list') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
class RegisterView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'room_detail.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
