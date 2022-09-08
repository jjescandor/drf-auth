from django.db import models
from django.contrib.auth import get_user_model

class EV_Car(models.Model):
    car_name = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    range = models.CharField(max_length=40)
    year = models.CharField(max_length=40)
    manufacturer = models.CharField(max_length=40)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.car_name