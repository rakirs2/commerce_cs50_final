from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def index(request):
    return render(request, "auctions/index.html", {
        "listings": AuctionListing.objects.all(),
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_listing(request):
    if request.method == "GET":
        return render(request, "auctions/new_listing.html", {
            "form": NewAuctionListing()
        })
    if request.method == "POST":
        # take in user data and save to form
        form = NewAuctionListing(request.POST);
        # validation
        if form.is_valid():
            # Extracting data

            seller = form.cleaned_data["seller"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            image_url = form.cleaned_data["image_url"]
            initial_bid = form.cleaned_data["initial_bid"]

            new_auction_listing = AuctionListing(seller=seller,
                                                 title=title,
                                                 description=description,
                                                 category=category,
                                                 image_url=image_url,
                                                 initial_bid=initial_bid)
            new_auction_listing.save()
            return HttpResponseRedirect(reverse("index"))


def product_page(request, product_id):
    if request.method == "GET":
        product = AuctionListing.objects.get(id=product_id)
        return render(request, "auctions/product.html", {
            "product": product,
        })

