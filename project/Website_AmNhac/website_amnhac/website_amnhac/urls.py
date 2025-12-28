"""
URL configuration for website_amnhac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from music import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("albums/", views.albums_store, name="albums"),
    path("events/", views.events, name="events"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_views, name="login"),
    path("register/", views.register_view, name="register"),
    path("customer/", views.customer, name="customer"),
    path("logout",views.logout_views, name="logout"),
    path('album/<int:album_id>/', views.albums_detail, name='albums_detail'),
    path("album_form/", views.add_form, name="add_form"),
    path("add_artist", views.add_artist, name="add_artist"),
    path("album/<int:album_id>/edit/", views.edit_album, name="edit_album"),
    path("album/<int:album_id>/delete/", views.delete_album, name="delete_album"),
    path('album/<int:album_id>/play/', views.play_first_song, name='play_first_song'),
    path("album/<int:album_id>/add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("orders/all/", views.all_orders, name="all_orders"),
    # Giỏ hàng
    path("cart/", views.cart, name="cart"),
    path("cart/update/<int:album_id>/", views.update_cart, name="update_cart"),
    path("cart/remove/<int:album_id>/", views.remove_from_cart, name="remove_from_cart"),
    #THanh toan
    path("checkout/", views.checkout, name="checkout"),
    path("checkout/success/<int:order_id>/", views.checkout_success, name="checkout_success"),
    #Account
    path("account/", views.account_view , name="account"),
]

# Phục vụ static files trong development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)