from django.db import models
import uuid
class offer (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    image1 = models.ImageField(upload_to="offers/", blank=True, null=True)
    image2 = models.ImageField(upload_to="offers/", blank=True, null=True)
    image3 = models.ImageField(upload_to="offers/", blank=True, null=True)
    image4 = models.ImageField(upload_to="offers/", blank=True, null=True)
    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    def __str__(self):
        return self.name
class Laptop(models.Model):
    model_name = models.CharField(max_length=255)
    price_syp = models.DecimalField(max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to='laptop_main_images/')  # Single main image

    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=50)
    hdd = models.CharField(max_length=50)
    gpu = models.CharField(max_length=255)
    screen = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)
    windows_version = models.CharField(max_length=255)

    def __str__(self):
        return self.model_name

class LaptopImage(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='images')  
    image = models.ImageField(upload_to='laptop_images/')  # Additional images

    def __str__(self):
        return f"Image for {self.laptop.model_name}"
# models.py

AGE_CHOICES = [
        ('جديد', 'جديد'),
        ('مستعمل', 'مستعمل'),
        ('اوبن بوكس', 'اوبن بوكس'),
    ]

class ProductType(models.Model):
    type = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')
    age = models.CharField(max_length=20, choices=AGE_CHOICES)
    status = models.BooleanField(default=True)
    count = models.IntegerField(default=0)

    # URL fields for external images
    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)
    url4 = models.URLField(blank=True)
    url5 = models.URLField(blank=True)

    # Local image upload fields
    image1 = models.ImageField(upload_to="products/", blank=True, null=True)
    image2 = models.ImageField(upload_to="products/", blank=True, null=True)
    image3 = models.ImageField(upload_to="products/", blank=True, null=True)
    image4 = models.ImageField(upload_to="products/", blank=True, null=True)
    image5 = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name

class DollarPrice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dollar_price = models.FloatField()