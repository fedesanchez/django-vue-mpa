from django.db import models


class Client(models.Model):

    STATUS_CHOICES = {
        "primary": "primary",
        "success": "success",
        "neutral": "neutral",
        "warning": "warning",
        "danger": "danger",
    }

    avatar = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)
    amount = models.FloatField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    date = models.DateTimeField() #if we add auto_now wil not be serialized on model_to_dict 

    def __str__(self) -> str:
        return self.name
