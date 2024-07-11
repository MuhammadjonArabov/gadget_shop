from apps.product.validators import phone_number_validator
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Memory(BaseModel):
    memory_size = models.CharField(max_length=225)

    def __str__(self):
        return self.memory_size


class Color(BaseModel):
    color_name = models.CharField(max_length=225)

    def __str__(self):
        return self.color_name


class ProductPictures(BaseModel):
    photo = models.ImageField(upload_to='product_image', blank=True, null=True)

    def __str__(self):
        return f"{self.id}"


class Product(BaseModel):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    YES = 1
    NO = 2
    EXISTENCE_TYPE_CHOICES = [
        (YES, "ha"),
        (NO, "yo'q")
    ]
    existence = models.PositiveIntegerField(choices=EXISTENCE_TYPE_CHOICES, default=YES)
    guarantee = models.CharField(max_length=225)
    deliver = models.CharField(max_length=225)
    acceptance = models.CharField(max_length=225)
    service_period = models.CharField(max_length=225)
    manufacturer = models.CharField(max_length=225)
    accessory = models.CharField(max_length=225)
