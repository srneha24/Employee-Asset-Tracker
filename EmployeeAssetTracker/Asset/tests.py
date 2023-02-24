from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

import json
from PIL import Image
from datetime import datetime, timedelta

# Create your tests here.
class AssetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_new_asset(self):
        url = reverse('NewAsset')

        data = {
            'name': 'HP Laptop',
            'quantity': 6
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['name'], 'HP Laptop')
        self.assertEqual(response.data['quantity'], 6)
    
    def test_new_delegation(self):
        url = reverse('NewDelegation')

        test_image_1 = Image.new('RGB', (100, 100), color='red')
        test_image_file_1 = SimpleUploadedFile('test_image_1.jpg', self.test_image.tobytes(), content_type='image/jpeg')
        test_image_2 = Image.new('RGB', (100, 100), color='blue')
        test_image_file_2 = SimpleUploadedFile('test_image_2.jpg', self.test_image.tobytes(), content_type='image/jpeg')

        data = {
            'employee': 1,
            'asset': 1,
            'delegation_time': datetime.now().strftime("%Y%m%d-%H:%M:%S"),
            'delegated_condition': "In perfect state",
            'delegated_condition_image': test_image_file_1,
            'assigned_return_time': datetime.now().strftime("%Y%m%d-%H:%M:%S") + timedelta(days=10),
            'actual_return_time': datetime.now().strftime("%Y%m%d-%H:%M:%S") + timedelta(days=3),
            'returned_condition': "Screen is cracked",
            'returned_condition_image': test_image_file_2
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_delegation_status(self):
        url = reverse('UpdateAssetStatus', args=[1])

        data = {
            'returned_condition': "Screen is cracked"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_asset_status(self):
        url = reverse('AssetStatus', args=[1])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
    
    def test_get_asset_status(self):
        url = reverse('AssetLog', args=[1])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
