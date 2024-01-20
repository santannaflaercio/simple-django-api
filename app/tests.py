# In app/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import ServiceEndpoint
from .serializers import ServiceEndpointSerializer


class ServiceEndpointModelTest(TestCase):
    """
    This class contains tests for the ServiceEndpoint model.
    It inherits from Django's TestCase class.
    """

    def test_create_and_retrieve_service_endpoint(self):
        """
        This test checks the creation and retrieval of a ServiceEndpoint instance.

        The test first creates a new ServiceEndpoint instance with a name and description.
        It then retrieves the first ServiceEndpoint instance from the database.

        The test asserts that the name and description of the retrieved instance match the ones provided during creation.
        """

        # Create a new ServiceEndpoint instance with a name and description
        ServiceEndpoint.objects.create(
            name="Test Endpoint", description="This is a test endpoint"
        )

        # Retrieve the first ServiceEndpoint instance from the database
        saved_endpoint = ServiceEndpoint.objects.first()

        # Assert that the name of the retrieved instance matches the one provided during creation
        self.assertEqual(saved_endpoint.name, "Test Endpoint")

        # Assert that the description of the retrieved instance matches the one provided during creation
        self.assertEqual(saved_endpoint.description, "This is a test endpoint")


class ServiceEndpointAPITest(APITestCase):
    """
    This class contains tests for the ServiceEndpoint API.
    It inherits from Django's APITestCase class.
    """

    def setUp(self):
        """
        This method sets up the test environment before each test method is run.
        It creates an instance of APIClient, which is used to make requests to the API.
        It also creates a dictionary containing the data for a new ServiceEndpoint instance,
        and makes a POST request to the 'serviceendpoint-list' URL to create a new ServiceEndpoint instance.
        The response from this request is stored in self.response.
        """
        self.client = APIClient()
        self.service_endpoint_data = {
            "name": "Test Endpoint",
            "description": "This is a test endpoint",
        }
        self.response = self.client.post(
            reverse("serviceendpoint-list"), self.service_endpoint_data, format="json"
        )

    def test_create_service_endpoint(self):
        """
        This test checks that a new ServiceEndpoint instance can be created via the API.
        It asserts that the status code of the response from the POST request made in setUp is 201 CREATED.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_service_endpoint(self):
        """
        This test checks that a ServiceEndpoint instance can be retrieved via the API.
        It first retrieves the ServiceEndpoint instance from the database,
        then makes a GET request to the 'serviceendpoint-detail' URL for that instance.
        It asserts that the status code of the response is 200 OK,
        and that the data returned in the response matches the data for the ServiceEndpoint instance.
        """
        service_endpoint = ServiceEndpoint.objects.get()
        response = self.client.get(
            reverse("serviceendpoint-detail", kwargs={"pk": service_endpoint.id}),
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = ServiceEndpointSerializer(service_endpoint)
        self.assertEqual(response.data, serializer.data)
