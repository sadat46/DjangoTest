from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=65)
    summery     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=True)
    upload      = models.FileField(upload_to='',blank=True)
    
