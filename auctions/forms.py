from django import forms
from .models import *


class NewAuctionListing(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = "__all__"


class NewWatchlistEntry(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = []
