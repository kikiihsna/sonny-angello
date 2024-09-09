from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  
    price = models.IntegerField()
    description = models.TextField()  
    stock = models.PositiveIntegerField()  
    image = models.ImageField(upload_to='product_images/', blank=True, null=True) 
    rarity = models.CharField(max_length=50, choices=[('common', 'Common'), ('rare', 'Rare'), ('ultra-rare', 'Ultra Rare')], default='common')  # Tingkat kelangkaan produk

    def __str__(self):
        return self.name
