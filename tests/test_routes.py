# tests/test_routes.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from your_app.models import Product  # Replace 'your_app' with your actual app name
from django.contrib.auth.models import User  # If authentication is used
from rest_framework.authtoken.models import Token

class ProductRoutesTests(APITestCase):
    def setUp(self):
        # Create a user if authentication is used
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # Create test products
        self.product1 = Product.objects.create(name='Product1', category='Category1', availability=True)
        self.product2 = Product.objects.create(name='Product2', category='Category2', availability=False)

    def test_list_all_products(self):
        url = reverse('list_all_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Adjust based on your actual data

    def test_list_by_name(self):
        url = reverse('list_by_name', kwargs={'name': 'Product1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_by_category(self):
        url = reverse('list_by_category', kwargs={'category': 'Category1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_by_availability(self):
        url = reverse('list_by_availability', kwargs={'availability': True})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Add more tests for other functions (Read, Update, Delete) as needed
