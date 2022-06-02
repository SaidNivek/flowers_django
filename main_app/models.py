from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add a relationship for the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

SEED_CHOICES = (
    ('bulb', 'Bulb'),
    ('seed', 'Seed'),
    ('tuber', 'Tuber'),
    ('corm', 'Corm'),
    ('rhyzome', 'Rhyzome')
)

class Seed(models.Model):
    seed_type = models.CharField(
        max_length=7,
        choices = SEED_CHOICES,
        default = 'seed'
        )
    seed_count = models.IntegerField(default=1)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name="seeds")

    def __str__(self):
        return f"{self.flower.name} {self.seed_type}"

class Garden(models.Model):
    garden_name = models.CharField(max_length=150)
    flowers = models.ManyToManyField(Flower)

    def __str__(self):
        return self.garden_name
