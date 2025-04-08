INSTALLED_APPS += [
    'tracker',
    'rest_framework',
    'dj_rest_auth',
    'django.contrib.sites',  # Required for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')  # Add CORS middleware

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["*"]

ALLOWED_HOSTS = ["*"]  # Allow all hosts

SITE_ID = 1  # Required for django-allauth