from rest_framework import serializers
from .models import User , Listing ,Review ,Booking
from django.contrib.auth.hashers import make_password
from rest_framework.validators import ValidationError


class UserSerial(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length = 100)
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password":{"write_only":True}}
        
        
    def create(self, validated_data):
        pword = validated_data.pop("password")
        cpword = validated_data.pop("confirm_password")
        if cpword != pword:
            raise ValidationError("password not the same")
        
        validated_data["password"] = make_password(pword)
        
        
        
        return super().create(validated_data)
    
    

class ListingSerial(serializers.ModelSerializer):
    host = serializers.SerializerMethodField()
    
    class Meta:
        model = Listing
        fields = "__all__"
        
    
    def get_host(self , obj):
        
        return obj.host_id.username 
    
    

class BookingSerial(serializers.ModelSerializer):
    guest = serializers.SerializerMethodField()
    property = Listing(read_only = True , source = "user_id")
    class Meta:
        model = Booking
        fields = "__all__"
        
    
    def get_guest(self , obj):
        
        return obj.user_id.username
        
        

class ReviewSerial(serializers.ModelSerializer):
    
    property = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = "__all__"
        
        
    def get_property(self , obj):
        return obj.property_id.name
    
    