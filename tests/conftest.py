import pytest
from rest_framework.test import APIClient
from apps.authentication.models import User


@pytest.fixture
def api_client():
    """
    Fixture for DRF API client
    """
    return APIClient()


@pytest.fixture
def test_user(db):
    """
    Fixture to create a test user
    """
    return User.objects.create_user(
        email='testuser@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )


@pytest.fixture
def authenticated_client(api_client, test_user):
    """
    Fixture for authenticated API client
    """
    api_client.force_authenticate(user=test_user)
    return api_client
