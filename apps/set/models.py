from django.db import models
from apps.product.models import BaseModel, Product


class Set(BaseModel):
    VIP = 1
    STANDARD = 2
    MINI = 3
    SET_TYPE_CHOICES = [
        (VIP, "vip"),
        (STANDARD, "standart"),
        (MINI, "mini"),
    ]
    set_type = models.PositiveIntegerField(choices=SET_TYPE_CHOICES, default=VIP)
    price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    saved_price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    product = models.ForeignKey(Product, related_name='product_set', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}"


class Set_Order(BaseModel):
    quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    unit_price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    total_amount = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    set = models.ForeignKey(Set, related_name='set_set_order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_set_order', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
