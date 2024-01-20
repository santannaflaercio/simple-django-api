from rest_framework import serializers
from .models import ServiceEndpoint


class ServiceEndpointSerializer(serializers.ModelSerializer):
    """
    This class represents the serializer for the ServiceEndpoint model.
    It inherits from Django Rest Framework's ModelSerializer, which provides default
    create, retrieve, update and delete operations.

    The Meta class within provides metadata for the serializer.
    """

    class Meta:
        """
        This class provides metadata for the ServiceEndpointSerializer.
        It is a nested class within the ServiceEndpointSerializer class.

        The 'model' attribute specifies the model class that this serializer should use.
        The 'fields' attribute specifies the fields that should be included in the serialized representation.
        '__all__' means all fields of the model will be included.
        """

        model = ServiceEndpoint
        fields = "__all__"
