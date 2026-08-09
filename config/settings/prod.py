"""운영 설정."""

from .base import *  # noqa: F403
from .base import get_env

DEBUG = False

ALLOWED_HOSTS = get_env("DJANGO_ALLOWED_HOSTS").split(",")

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
