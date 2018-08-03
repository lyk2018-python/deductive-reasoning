from django.db import models
from proofs.models import *
from django.conf import settings

class Comment(models.Model):
    modelObject=models.ForeignKey(Proof,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    text=models.TextField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text


# Create your models here.
