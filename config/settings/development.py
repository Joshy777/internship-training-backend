"""
Development settings
"""
from .base import *  # noqa: F403, F401

DEBUG = True

INSTALLED_APPS += [  # noqa: F405
    'django_extensions',
]

# Django Debug Toolbar
if DEBUG:  # noqa: F405
    INSTALLED_APPS += ['debug_toolbar']  # noqa: F405
    MIDDLEWARE += [  # noqa: F405
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    INTERNAL_IPS = ['127.0.0.1']
