import factory

# Import your model class for Product
from .models import Product  # Replace with the correct import path

# If using Faker, import it as well
from faker import Faker

class ProductFactory(factory.Factory):

    class Meta:
        model = Product  # Specify the model to create instances of

    # Define fields and their default values using Faker or hardcoded values:
    name = factory.Faker('name')  # Example using Faker
    price = factory.Faker('pydecimal', left_digits=2, right_digits=2)
    description = factory.Faker('paragraph')
    category = factory.Faker('word')
    availability = factory.Faker('boolean')

    # Optionally, define strategies for certain fields:
    @factory.post_generation
    def set_images(self, create, extracted, **kwargs):
        if create:
            # Add logic to create and assign images to the product
            pass

