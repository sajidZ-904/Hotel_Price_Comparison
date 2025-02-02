from django.db import models
from django.conf import settings  # Ensures correct user model reference

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    star_rating = models.DecimalField(max_digits=2, decimal_places=1)
    price_booking = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_agoda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    booking_url = models.URLField(null=True, blank=True)
    agoda_url = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100)
    bookmarked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmarked_hotels', blank=True)

    def best_price(self):
        """Returns the lowest available price between Booking.com and Agoda."""
        prices = [p for p in [self.price_booking, self.price_agoda] if p is not None]
        return min(prices) if prices else None

    def __str__(self):
        return f"{self.name} - {self.city}"
