from django.db import models
from accounts.models import CustomUser
from products.models import Product
from django.core.validators import MinValueValidator


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'role':'customer'})
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    complete_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.username} ordered for {self.product}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity  = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])

    @property
    def amount_pay(self):
        product_price = self.product.price
        return product_price*self.quantity
    
    @property
    def customer(self):
        return self.order.customer.username
    
    @property
    def vendor(self):
        return self.product.vendor.username

    def __str__(self):
        return f"{self.product.name} Ordered By {self.customer}"