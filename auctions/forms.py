from django import forms
from .models import AuctionListing


class NewAuctionListing(forms.Form):
    class Meta:
        model = AuctionListing
        fields = "__all__"
