from rest_framework.routers import DefaultRouter
from .views import ListingViewset


router = DefaultRouter()

router.register("listings", ListingViewset, basename="listings")


urlpatterns = router.urls
