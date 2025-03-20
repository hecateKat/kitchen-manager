from django.contrib.auth.models import AbstractUser
from django.forms import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"



class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)

    def __str__(self):
        return f"{self.name} ({self.dish_type})"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.CharField(max_length=50)
