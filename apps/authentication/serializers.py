from rest_framework import serializers
from django.contrib.auth import authenticate  # noqa: F401
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model - used for responses

    TODO for Interns:
    - Define the Meta class with appropriate fields
    - Decide which fields should be read-only
    - Consider what user information should be exposed via API
    """
    class Meta:
        model = User
        # TODO: Add fields here
        # Hint: id, email, first_name, last_name, date_joined
        fields = '__all__'  # REPLACE THIS - be specific about fields
        read_only_fields = ('id', 'date_joined')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration

    TODO for Interns:
    1. Add password and password_confirm fields as write_only
    2. Implement validate() method to check if passwords match
    3. Implement create() method to create user with hashed password
    4. Consider: What validations are needed? Email format? Password strength?
    """
    # TODO: Add password fields here
    # password = serializers.CharField(...)
    # password_confirm = serializers.CharField(...)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')  # TODO: Add password_confirm

    def validate(self, attrs):
        """
        TODO: Implement password matching validation
        Hint: Check if password == password_confirm
        Raise serializers.ValidationError if they don't match
        """
        # Your code here
        return attrs

    def create(self, validated_data):
        """
        TODO: Implement user creation
        Hint:
        - Remove password_confirm from validated_data
        - Use User.objects.create_user() to properly hash the password
        - Return the created user
        """
        # Your code here
        pass


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login

    TODO for Interns:
    1. Define email and password fields
    2. Implement validate() method to authenticate user
    3. Return the authenticated user in validated_data
    4. Handle errors: invalid credentials, inactive user
    """
    # TODO: Define fields here
    # email = serializers.EmailField()
    # password = serializers.CharField(...)

    def validate(self, attrs):
        """
        TODO: Implement authentication logic
        Steps:
        1. Get email and password from attrs
        2. Use authenticate() to verify credentials
        3. Check if user is active
        4. Add user to attrs['user']
        5. Return attrs

        Resources:
        - Django authenticate:
          https://docs.djangoproject.com/en/5.0/topics/auth/default/
        """
        # Your code here
        pass
