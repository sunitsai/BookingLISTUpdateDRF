from rest_framework import serializers
from .models import *


class ListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('listing_type','title','country','city')

class BookingInfoSerializers(serializers.ModelSerializer):
    # listing = serializers.StringRelatedField(read_only=True)
    # listing = ListingSerializers()
    listing_type = serializers.ReadOnlyField(source='listing.listing_type',read_only=True)
    title = serializers.ReadOnlyField(source='listing.title',read_only=True)
    country = serializers.ReadOnlyField(source='listing.country',read_only=True)
    city = serializers.ReadOnlyField(source='listing.city',read_only=True)
    
    class Meta:
        model = BookingInfo
        fields = ('price','listing_type','title','country','city')
    

# class BookingInfoHotelSerializers(serializers.ModelSerializer):
#     hotel_room_type = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = BookingInfo
#         fields = ('id','price','hotel_room_type')
    