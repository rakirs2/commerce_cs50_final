from django import forms
from .models import AuctionListing


class NewAuctionListing(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = "__all__"
