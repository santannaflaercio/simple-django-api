from django.db import models


class ServiceEndpoint(models.Model):
    """
    This class represents the ServiceEndpoint model.
    It inherits from Django's Model class, which provides functionality for interacting with the database.
    """

    # The name attribute is a CharField, which is a string field in Django.
    # It has a maximum length of 100 characters.
    name = models.CharField(max_length=100)

    # The description attribute is a TextField, which is a large text field in Django.
    description = models.TextField()

    class Meta:
        """
        This class provides metadata for the ServiceEndpoint model.
        It is a nested class within the ServiceEndpoint model class.
        """

        # The app_label attribute specifies the name of the application that this model belongs to.
        app_label = "app"
