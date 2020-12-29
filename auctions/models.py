from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    title = models.CharField(max_length=50, blank=False, unique=True)
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=2056)
    category = models.CharField(max_length=20, blank=True)
    image_url = models.URLField()

    def __str__(self):
        return f"""id=:{self.id}
        seller:{self.seller}
        title:{self.title}
        category:{self.category}
        image_url:{self.image_url}
        """
