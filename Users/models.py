from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class customuser(AbstractUser):
    product_manager= models.BooleanField(default=False)
    cart_manager= models.BooleanField(default=False)

def __str__(self):
        return self.username