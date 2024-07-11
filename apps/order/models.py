from apps.product.validators import phone_number_validator
from django.db import models
from django.utils import timezone
from apps.product.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Order_code(BaseModel):
    deliver_price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    coupon_code = models.CharField(max_length=225)
    promo_code = models.CharField(max_length=225)
    user = models.OneToOneField(User, related_name='user_order_code', on_delete=models.SET_NULL)

    def __str__(self):
        return self.promo_code


class Order(BaseModel):
    GO_GET = 1
    HANDLE = 2
    DELIVER_TYPE_CHOICES = [
        (GO_GET, "borib olish"),
        (HANDLE, "dostavka")
    ]
    CASH = 1
    CLICK = 2
    PAYME = 3
    PAYMENT_TYPE_CHOICES = [
        (CASH, 'cash'),
        (CLICK, 'click'),
        (PAYME, 'payme')
    ]
    deliver_type = models.PositiveIntegerField(choices=DELIVER_TYPE_CHOICES, default=HANDLE)
    payment_type = models.PositiveIntegerField(choices=PAYMENT_TYPE_CHOICES, default=CLICK)
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE)
    order_code = models.OneToOneField(Order_code, related_name='order_code_Order', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}"
