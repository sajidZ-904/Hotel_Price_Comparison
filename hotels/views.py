from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .forms import HotelSearchForm

def search_hotels(request):
    """Handles hotel search by city, price range, and star rating."""
    form = HotelSearchForm(request.GET or None)
    hotels = []

    if form.is_valid():
        city = form.cleaned_data['city']
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']
        star_rating = form.cleaned_data['star_rating']

        hotels = Hotel.objects.filter(
            city__iexact=city,
            star_rating__gte=star_rating,
            price_booking__gte=min_price, price_booking__lte=max_price
        ) | Hotel.objects.filter(
            city__iexact=city,
            star_rating__gte=star_rating,
            price_agoda__gte=min_price, price_agoda__lte=max_price
        )

    return render(request, 'hotels/search.html', {'form': form, 'hotels': hotels})

@login_required
def bookmark_hotel(request, hotel_id):
    """Allows users to bookmark a hotel."""
    hotel = get_object_or_404(Hotel, id=hotel_id)
    user = request.user

    if hotel.bookmarked_by.filter(id=user.id).exists():
        hotel.bookmarked_by.remove(user)  # Unbookmark if already bookmarked
    else:
        hotel.bookmarked_by.add(user)  # Bookmark hotel

    return redirect('bookmarks')

@login_required
def view_bookmarks(request):
    """Displays a list of bookmarked hotels."""
    hotels = request.user.bookmarked_hotels.all()
    return render(request, 'hotels/bookmarks.html', {'hotels': hotels})
