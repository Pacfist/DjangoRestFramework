import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Color(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class BaseProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    base_product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    @property
    def in_stock(self):
        return (self.stock or 0) > 0
    
    def __str__(self):
        return self.name

    
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    products = models.ManyToManyField(Product, through="OrderItem", related_name='orders')

    def __str__(self):
        return f"Order {self.order_id } by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_id}"