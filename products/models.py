from django.db import models

# Create your models here.
class Cameralar(models.Model):
    make = models.CharField(max_length=30)
    resolution = models.CharField(max_length=20, default='24MP')
    zoom = models.CharField(max_length=20, default='20x')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='camera-image/', blank=True, null=True, default='default/camere.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.make


