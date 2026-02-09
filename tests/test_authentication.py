import pytest
from django.urls import reverse
from rest_framework import status
from apps.authentication.models import User


@pytest.mark.django_db
class TestRegistration:
    """
    Test cases for user registration
    """

    def test_register_user_success(self, api_client):
        url = reverse('register')
        data = {
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'strongpass123',
            'password_confirm': 'strongpass123'
        }
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert 'user' in response.data
        assert response.data['user']['email'] == data['email']
        assert User.objects.filter(email=data['email']).exists()

    def test_register_user_password_mismatch(self, api_client):
        url = reverse('register')
        data = {
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'strongpass123',
            'password_confirm': 'differentpass123'
        }
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestLogin:
    """
    Test cases for user login
    """

    def test_login_success(self, api_client, test_user):
        url = reverse('login')
        data = {
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert 'tokens' in response.data
        assert 'access' in response.data['tokens']
        assert 'refresh' in response.data['tokens']
        assert 'user' in response.data

    def test_login_invalid_credentials(self, api_client, test_user):
        url = reverse('login')
        data = {
            'email': 'testuser@example.com',
            'password': 'wrongpassword'
        }
        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestMeEndpoint:
    """
    Test cases for /me endpoint
    """

    def test_get_current_user_authenticated(self, authenticated_client, test_user):
        url = reverse('me')
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == test_user.email
        assert response.data['first_name'] == test_user.first_name

    def test_get_current_user_unauthenticated(self, api_client):
        url = reverse('me')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
