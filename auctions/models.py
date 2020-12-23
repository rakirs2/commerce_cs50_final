from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster");
    title = models.CharField(max_length=50, blank=False, unique=True);
    id = models.AutoField(primary_key=True);
