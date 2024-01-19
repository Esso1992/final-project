# features/steps/load_steps.py
from behave import given, when, then
from service.models import Product  # Adjust the import based on your actual model

@given("the following products exist")
def step_given_products_exist(context):
    for row in context.table:
        # Assuming your Product model has fields 'name', 'category', 'availability', etc.
        Product.objects.create(
            name=row["name"],
            category=row["category"],
            availability=row["availability"],
            # Add other fields as needed
        )

@when("I load the BDD data")
def step_when_load_bdd_data(context):
    pass  # You may add implementation if needed

@then("the BDD data should be loaded successfully")
def step_then_bdd_data_loaded_successfully(context):
    # Add assertions or checks to ensure data is loaded successfully
    assert Product.objects.count() == len(context.table.rows), "Unexpected number of products"
    # Add more assertions as needed

