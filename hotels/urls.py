from django.urls import path
from .views import search_hotels, bookmark_hotel, view_bookmarks

urlpatterns = [
    path('search/', search_hotels, name='search_hotels'),
    path("bookmark/<int:hotel_id>/", bookmark_hotel, name="bookmark_hotel"),
    path("bookmarks/", view_bookmarks, name="view_bookmarks"),
]
