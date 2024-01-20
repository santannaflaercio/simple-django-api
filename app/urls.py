from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ServiceEndpointViewSet

# Create an instance of the DefaultRouter class
router = DefaultRouter()

# Register the ServiceEndpointViewSet with the router
# The first argument is the URL prefix for the routes created by the router
# The second argument is the viewset class
# The third argument is the basename used to generate the URL names
router.register(r'service-endpoints', ServiceEndpointViewSet, basename='serviceendpoint')

# Define the URL patterns for the app
# The include function is used to include the URLs created by the router
urlpatterns = [
    path('', include(router.urls)),
]
