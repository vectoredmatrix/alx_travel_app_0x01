from rest_framework.routers import DefaultRouter
from .views import ListingViewset , BookingViewSet


router = DefaultRouter()

router.register("listings", ListingViewset, basename="listings")
router.register("bookings" , BookingViewSet , basename="bookings")

urlpatterns = router.urls
