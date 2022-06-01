from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']