from django.contrib import admin
        # ticketingapp/admin.py
        
from .models import Customer, Venue, Event, TicketTypes, Orders, OrderItem # Import all your models

admin.site.register(Customer)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(TicketTypes)
admin.site.register(Orders)
admin.site.register(OrderItem)

# Register your models here.
