from django.contrib import admin
from classes.models import Restaurant, Faculty, Restaurant_food, Food
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Faculty)
admin.site.register(Restaurant_food)
admin.site.register(Food)