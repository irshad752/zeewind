from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class Product(models.Model):

    CATEGORY_CHOICES = (
        ('Ceiling', 'Ceiling Fan'),
        
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.IntegerField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class ProductColorImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
    color_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_colors/')

    def __str__(self):
        return f"{self.product.name} - {self.color_name}"
    

class WarrantyRegistration(models.Model):
        PRODUCT_CHOICES = [
            ('Maavel','Maavel'),
            ('Atmos Pro','Atmos Pro'),
            ('Spin Air','Spin Air'),
            ('Atmos Silent','Atmos Silent'),
            ('Max Air','Max Air'),
            ('Dazzale','Dazzale'),
        ]
        COLOR_CHOICES = [
            ('White','White'),
            ('Black','Black'),
            ('Brown','Brown'),
            ('Ivory','Ivory'),
        ]

        product_name = models.CharField(max_length=50, choices=PRODUCT_CHOICES)
        product_color = models.CharField(max_length=30, choices=COLOR_CHOICES)
        name = models.CharField(max_length=100)
        phone = models.CharField(max_length=10)
        email = models.EmailField()
        address = models.TextField()
        serial_number = models.CharField(max_length=50, unique=True)
        date_of_purchase = models.DateField()
        submitted_at = models.DateTimeField(auto_now_add=True)
        is_verified = models.BooleanField(default=False)

        def __str__(self):
             return f"{self.name} - {self.product_name} ({self.serial_number})"
class WarrantyApproval(models.Model):
    registration = models.OneToOneField(WarrantyRegistration, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
         return f"Approvals for {self.registration.serial_number}"


    def warranty_end_date(self):
        if self.registration.date_of_purchase:
             return self.registration.date_of_purchase + timedelta(days=730)  # 2 years
             return None
