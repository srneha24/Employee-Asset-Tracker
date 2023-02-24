from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

import json

# Create your tests here.

class CompanyTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_new_company(self):
        url = reverse('AddCompany')

        data = {
            'username': 'starktech',
            'company_name': 'Stark Technologies',
            'password': 'peaceinourtime'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['username'], 'starktech')
        self.assertEqual(response.data['company_name'], 'Stark Technologies')

    def test_company_login(self):
        url = reverse('CompanyLogin')

        data = {
            'username': 'starktech',
            'password': 'peaceinourtime'
        }

        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

class EmployeeTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post(self):
        url = reverse('Employee')

        session = self.client.session
        session["company"] = 1
        session.save()

        data = {
            'employee_name': 'Quentin Beck',
            'designation': 'BARF Developer'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['employee_name'], 'Quentin Beck')
        self.assertEqual(response.data['designation'], 'BARF Developer')

    def test_get(self):
        url = reverse('Employee', args=[1])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
