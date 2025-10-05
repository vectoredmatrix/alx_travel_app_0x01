from django.shortcuts import render
from .serializers import ListingSerial , BookingSerial
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Listing , Booking
from .paginations import LargeResultsSetPagination
# Create your views here.


class ListingViewset(ModelViewSet):
    serializer_class = ListingSerial
    pagination_class = LargeResultsSetPagination
    
    def get_queryset(self):
        user = self.request.user
        print(user.username)
        listings = Listing.objects.filter(host_id = user.pk).select_related("host_id")
        
        return listings
    
class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerial
    pagination_class = LargeResultsSetPagination
    
    def get_queryset(self):
        
        userbookings = Booking.objects.filter(user_id = self.request.user).select_related("user_id" , "property_id")
        
        return userbookings

