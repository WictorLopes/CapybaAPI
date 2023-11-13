
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model

class RegistrationTestCase(TestCase):
    def test_user_registration(self):
        client = APIClient()
        response = client.post('/api/register/', {'email': 'admin@admin.com', 'password': '123'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_duplicate_user_registration(self):
    #     client = APIClient()
    #     response = client.post('/api/register/', {'email': 'admin@admin.com', 'password': '123'})
    #     self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)


class AuthenticationTestCase(TestCase):
    def test_user_login_logout(self):
        client = APIClient()
        login_response = client.post('/api/login/', {'email': 'admin@admin.com', 'password': '123'})
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        logout_response = client.post('/api/logout/')
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)


class RestrictedItemsTestCase(TestCase):
    def test_restricted_items_list(self):
        client = APIClient()
        client.post('/api/login/', {'email': 'admin@admin.com', 'password': '123'})

        response = client.get('/api/restricted-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_profile_edit(self):
    client = APIClient()
    client.post('/api/login/', {'email': 'admin@admin.com', 'password': '123'})

    response = client.put('/api/edit-profile/', {'email': 'new@example.com'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmailConfirmationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@admin.com',
            password='123'
        )

    def test_email_confirmation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/send-email-confirmation-token/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class EmailTokenValidationTestCase(TestCase):
    def test_email_token_validation(self):
        client = APIClient()
        send_token_response = client.post('/api/send-email-confirmation-token/')
        self.assertEqual(send_token_response.status_code, status.HTTP_200_OK)
        token = "exemplo_token_gerado_pelo_sistema"
        
        validation_response = client.post('/api/validate-email-confirmation-token/', {'token': token})
        self.assertEqual(validation_response.status_code, status.HTTP_200_OK)
