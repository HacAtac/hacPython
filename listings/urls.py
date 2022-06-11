from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    # <int:listing_id> allows us to pass in a number as a parameter
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]