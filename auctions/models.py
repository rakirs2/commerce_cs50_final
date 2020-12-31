from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    title = models.CharField(max_length=50, blank=False, unique=True)
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=2056)
    initial_bid = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.CharField(max_length=20, blank=True)
    image_url = models.URLField()

    def __str__(self):
        return f"""id=:{self.id}
        seller:{self.seller}
        title:{self.title}
        category:{self.category}
        image_url:{self.image_url}
        """


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    bid_value = models.DecimalField(decimal_places=2, max_digits=15)
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="listing")


class Watchlist(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="item")

    def __str__(self):
        return f"""buyer: {self.buyer}
        auction_listing: {self.auction_listing}
        """