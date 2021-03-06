from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("product/<int:product_id>", views.product_page, name="product_page"),
    path("add_to_watchlist/<int:product_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("user_home", views.view_user_home, name="user_home"),
]
