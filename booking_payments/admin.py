from django.contrib import admin
from .models import Booking, Payment

class BookingAdmin(admin.ModelAdmin):
  list_display = ("room", "check_in",)
  list_filter = ['room']


class PaymentAdmin(admin.ModelAdmin):
  list_display = ("payment_mode", "payment_type",)
  list_filter = ['payment_mode']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)

