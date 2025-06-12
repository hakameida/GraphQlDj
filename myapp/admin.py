from django.contrib import admin
from .models import Laptop ,offer, LaptopImage , ProductType , Product,DollarPrice

# admin.site.register(Laptop)  # Registers the model for admin panel
# admin.site.register(LaptopImage)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(DollarPrice)
admin.site.register(offer)
