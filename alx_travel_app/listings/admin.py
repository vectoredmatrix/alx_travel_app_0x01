from django.contrib import admin

# Register your models here.
from .models import User , Listing , Review , Booking



class userAdmin(admin.ModelAdmin):
    list_display =["username" , "role","phone_number"]
  
  
class listingAmdin(admin.ModelAdmin):
    list_display=["name" , "host_id" ,"pricepernight"]  
    

class bookingAdmin(admin.ModelAdmin):
    list_display = ["property_id" , "user_id" ,"status" ]

admin.site.register(User , userAdmin)
admin.site.register(Listing , listingAmdin)
admin.site.register(Booking , bookingAdmin)