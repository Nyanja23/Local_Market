from django.db import models
from accounts.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    description = models.TextField(blank=True)
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role':'vendor'})

    def __str__(self):
        return f"{self.name} Owned by {self.vendor.username}"