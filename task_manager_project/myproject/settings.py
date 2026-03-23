import os
from pathlib import Path

# This tells Django where your main folder is located
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key (required for Django to work)
SECRET_KEY = 'django-insecure-task-manager-key'

# Debug mode should be True while you are building
DEBUG = True

ALLOWED_HOSTS = []

# This is where you register your 'tasks' app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks', 
]

# This tells Django to look for your HTML in the 'templates' folder
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# This tells Django where the SQL database file will be saved
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}