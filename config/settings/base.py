"""공통 설정.

개발 설정은 dev.py, 운영 설정은 prod.py에서 이 파일을 불러온다.
비밀 값은 코드에 넣지 않고 환경 변수로 주입한다.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


def get_env(name: str, default: str | None = None) -> str:
    """환경 변수를 읽는다.

    Args:
        name: 환경 변수 이름
        default: 값이 없을 때 사용할 기본값

    Returns:
        환경 변수 값

    Raises:
        RuntimeError: 값이 없고 기본값도 없을 때
    """
    value = os.environ.get(name, default)
    if value is None:
        raise RuntimeError(f"환경 변수 {name}을(를) 설정해야 합니다.")
    return value


SECRET_KEY = get_env("DJANGO_SECRET_KEY")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env("DB_NAME", "haedal_rental"),
        "USER": get_env("DB_USER", "postgres"),
        "PASSWORD": get_env("DB_PASSWORD", ""),
        "HOST": get_env("DB_HOST", "localhost"),
        "PORT": get_env("DB_PORT", "5432"),
    }
}

_PASSWORD_VALIDATION = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{_PASSWORD_VALIDATION}.UserAttributeSimilarityValidator"},
    {"NAME": f"{_PASSWORD_VALIDATION}.MinimumLengthValidator"},
    {"NAME": f"{_PASSWORD_VALIDATION}.CommonPasswordValidator"},
    {"NAME": f"{_PASSWORD_VALIDATION}.NumericPasswordValidator"},
]

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
