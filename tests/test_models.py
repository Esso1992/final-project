# tests/test_models.py
from django.test import TestCase
from your_app.models import Product  # Replace 'your_app' with your actual app name

class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create some sample products for testing
        Product.objects.create(name='Product1', category='Category1', availability='In Stock', price=10.99)
        Product.objects.create(name='Product2', category='Category2', availability='Out of Stock', price=15.99)

    def test_read_product(self):
        product = Product.objects.get(name='Product1')
        self.assertEqual(product.category, 'Category1')

    def test_update_product(self):
        product = Product.objects.get(name='Product1')
        product.price = 20.99
        product.save()
        updated_product = Product.objects.get(name='Product1')
        self.assertEqual(updated_product.price, 20.99)

    def test_delete_product(self):
        product = Product.objects.get(name='Product1')
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(name='Product1')

    def test_list_all_products(self):
        products = Product.objects.all()
        self.assertEqual(products.count(), 2)

    def test_find_by_name(self):
        product = Product.objects.get(name='Product1')
        self.assertEqual(product.category, 'Category1')

    def test_find_by_category(self):
        products = Product.objects.filter(category='Category2')
        self.assertEqual(products.count(), 1)

    def test_find_by_availability(self):
        products = Product.objects.filter(availability='In Stock')
        self.assertEqual(products.count(), 1)
