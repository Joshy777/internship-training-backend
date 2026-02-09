# Internship Training Backend - Django REST API

## Overview
This is the backend API for the internship training program. It demonstrates:
- Django REST Framework best practices
- JWT authentication
- Custom User model with email authentication
- Test-driven development
- Git workflow and CI/CD integration

## Tech Stack
- Python 3.11+
- Django 5.0
- Django REST Framework
- PostgreSQL (Production) / SQLite (Development)
- JWT Authentication
- pytest for testing

## Quick Start

### Prerequisites
- Python 3.11 or higher
- pip and virtualenv
- Git

### Installation
```bash
# Clone the repository
git clone <repo-url>
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/development.txt

# Setup environment variables
cp .env.example .env
# Edit .env file with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login (returns JWT tokens)
- `POST /api/auth/refresh/` - Refresh access token
- `GET /api/auth/me/` - Get current user (requires authentication)

### Example Login Request
```json
POST /api/auth/login/
{
  "email": "user@example.com",
  "password": "securepassword"
}

Response:
{
  "user": {
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbG...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbG..."
  }
}
```

## Development Workflow

### Branch Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/<feature-name>` - Feature branches
- `bugfix/<bug-name>` - Bug fix branches

### Commit Convention
```
feat: add user registration endpoint
fix: resolve JWT token expiration issue
docs: update API documentation
test: add authentication tests
refactor: improve serializer structure
```

### Pull Request Process
1. Create feature branch from `develop`
2. Make changes with conventional commits
3. Write/update tests
4. Ensure all tests pass: `pytest`
5. Run linting: `flake8 .` and `black .`
6. Push and create PR to `develop`
7. Request code review
8. Merge after approval

## Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=apps

# Run specific test file
pytest tests/test_authentication.py
```

## Code Quality
```bash
# Format code
black apps/ config/

# Sort imports
isort apps/ config/

# Lint code
flake8 apps/ config/
```

## Environment Variables
See `.env.example` for required environment variables.

## Project Structure
```
apps/
  authentication/  - User authentication and JWT handling
  core/           - Shared utilities, middleware, permissions
config/
  settings/       - Environment-specific settings
  urls.py         - Root URL configuration
tests/            - Test suite
```

## Learning Objectives
- Understand Django REST Framework architecture
- Implement JWT authentication
- Write API tests with pytest
- Follow Git branching strategy
- Practice code review process
- Configure CI/CD pipelines

## Troubleshooting
- **Migration issues**: `python manage.py migrate --run-syncdb`
- **Token errors**: Check JWT settings in config/settings/base.py
- **CORS errors**: Verify CORS_ALLOWED_ORIGINS in .env

## Resources
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## Support
For issues or questions, create an issue in the repository or contact your mentor.
