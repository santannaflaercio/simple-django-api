from rest_framework import viewsets
from .models import ServiceEndpoint
from .serializers import ServiceEndpointSerializer


class ServiceEndpointViewSet(viewsets.ModelViewSet):
    """
    This class represents a viewset for the ServiceEndpoint model.
    It inherits from Django Rest Framework's ModelViewSet, which provides default
    'create', 'retrieve', 'update', 'partial_update', 'destroy' and 'list' actions.
    """

    # The queryset attribute is a collection of objects from the ServiceEndpoint model.
    # The .all() method returns all instances of the model.
    queryset = ServiceEndpoint.objects.all()

    # The serializer_class attribute is a reference to the serializer class
    # that should be used for serializing and deserializing instances of the ServiceEndpoint model.
    serializer_class = ServiceEndpointSerializer
