from django.db import models
 # myapp/models.py
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    # ... other fields
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)         
    capacity = models.IntegerField()
    # ... other fields
    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    # ... other fields

    def __str__(self):
        return self.name
    
class TicketTypes(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # ... other fields

    def __str__(self):
        return self.name        
    
class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketTypes, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # ... other fields
    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketTypes, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # ... other fields
    def __str__(self):
        return f"Order Item #{self.id}"
    

# Create your models here.
