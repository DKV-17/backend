"""
 Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================================
 # SECURITY
 # =====================================================

SECRET_KEY = os.getenv(
 "SECRET_KEY",
 "django-insecure-change-this-key"
 )

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
"backend-1glw.onrender.com",
"127.0.0.1",
"localhost",
]

# Render Host
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
 ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# =====================================================
 # APPLICATIONS
 # =====================================================

INSTALLED_APPS = [

 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",

 # Third Party
 "rest_framework",
 "corsheaders",

 # Local Apps
 "students",

]

# =====================================================
 # MIDDLEWARE
 # =====================================================

MIDDLEWARE = [

 "django.middleware.security.SecurityMiddleware",

 # WhiteNoise
 "whitenoise.middleware.WhiteNoiseMiddleware",

 "corsheaders.middleware.CorsMiddleware",

 "django.contrib.sessions.middleware.SessionMiddleware",

 "django.middleware.common.CommonMiddleware",

 "django.middleware.csrf.CsrfViewMiddleware",

 "django.contrib.auth.middleware.AuthenticationMiddleware",

 "django.contrib.messages.middleware.MessageMiddleware",

 "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "config.urls"

# =====================================================
 # TEMPLATES
 # =====================================================

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

# =====================================================
 # DATABASE
 # =====================================================

DATABASES = {
 "default": dj_database_url.config(
 default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
 conn_max_age=600,
 )
 }

# =====================================================
 # DJANGO REST FRAMEWORK
 # =====================================================

REST_FRAMEWORK = {

 "DEFAULT_PERMISSION_CLASSES": [
 "rest_framework.permissions.AllowAny",
 ],

 "DEFAULT_RENDERER_CLASSES": [
 "rest_framework.renderers.JSONRenderer",
 ],
 }

# =====================================================
 # PASSWORD VALIDATION
 # =====================================================

AUTH_PASSWORD_VALIDATORS = [
 {
 "NAME":
 "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
 },
 {
 "NAME":
 "django.contrib.auth.password_validation.MinimumLengthValidator",
 },
 {
 "NAME":
 "django.contrib.auth.password_validation.CommonPasswordValidator",
 },
 {
 "NAME":
 "django.contrib.auth.password_validation.NumericPasswordValidator",
 },
 ]

# =====================================================
 # INTERNATIONALIZATION
 # =====================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# =====================================================
 # STATIC FILES
 # =====================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
 "whitenoise.storage.CompressedManifestStaticFilesStorage"
 )

# =====================================================
 # MEDIA FILES
 # =====================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# =====================================================
 # DEFAULT PRIMARY KEY
 # =====================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =====================================================
 # CORS
 # =====================================================

CORS_ALLOW_ALL_ORIGINS = ["https://frontend-nine-rho-77.vercel.app"]

CORS_ALLOW_CREDENTIALS = True

# =====================================================
 # CSRF
 # =====================================================

CSRF_TRUSTED_ORIGINS = [
 "http://localhost:5173","https://frontend-nine-rho-77.vercel.app/"
 ]

# =====================================================
 # SECURITY (Production)
 # =====================================================

if not DEBUG:

 SECURE_PROXY_SSL_HEADER = (
 "HTTP_X_FORWARDED_PROTO",
 "https",
 )

 SECURE_SSL_REDIRECT = True

 SESSION_COOKIE_SECURE = True

 CSRF_COOKIE_SECURE = True