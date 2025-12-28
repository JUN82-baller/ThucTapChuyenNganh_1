from encodings.punycode import selective_find

from django.db import models
from PIL import Image
import os
from django.conf import settings


class Artist(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    cover = models.ImageField(upload_to='albums', blank=True, null=True, max_length=255)
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        try:
            this = Album.objects.get(id=self.id)
            if this.cover and this.cover != self.cover:
                old_path = os.path.join(settings.MEDIA_ROOT, str(this.cover))
                if os.path.isfile(old_path):
                    os.remove(old_path)
        except Album.DoesNotExist:
            pass  # album mới, không cần xóa gì
        super().save(*args, **kwargs)


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    audio_file = models.FileField(upload_to='songs', blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True)  # duration of audio

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album.title} x {self.quantity} (User: {self.user.username})"

    @property
    def total_price(self):
        return self.album.price * self.quantity

class Order(models.Model):
    PAYMENT_CHOICES = [
        ("COD", "Thanh toán khi nhận hàng"),
        ("BANK", "Chuyển khoản ngân hàng"),
        ("CARD", "Thẻ tín dụng/ghi nợ"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        default="COD"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.name}"

    @property
    def get_total(self):
        # cộng dồn tất cả OrderItem của đơn hàng
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.album.title} x {self.quantity}"

    @property
    def total_price(self):
        return self.price * self.quantity

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Event(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='events/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.date}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonials',blank=True)

    def __str__(self):
       return f"{self.name} - {self.role}"
