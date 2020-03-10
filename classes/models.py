from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="gallery")
    open_time = models.TimeField()
    close_time = models.TimeField()
    rating = models.FloatField()
    approve_by = models.CharField(max_length=100)
    approve_date = models.DateField(null=True, blank=True, auto_now_add=True)

    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

class Food(models.Model):
    name = models.CharField(max_length=100)
    is_vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Restaurant_food(models.Model):
    price = models.FloatField(max_length=100)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    