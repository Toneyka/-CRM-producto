from pathlib import Path
from django.contrib.messages import constants as messages

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- direccion ---
SECRET_KEY = 'django-insecure-cambia-esta-clave-para-produccion'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# --- Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App local
    'inventario',
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# --- Templates ---
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        BASE_DIR / 'core' / 'templates',  
    
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]


WSGI_APPLICATION = 'core.wsgi.application'

# --- Base de datos (SQLite local) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Validadores de contraseña (podés simplificar en dev) ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --- Internacionalización ---
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Cordoba'
USE_I18N = True
USE_TZ = True

# --- Archivos estáticos ---
STATIC_URL = 'static/'

# --- Mensajes (Bootstrap mapping opcional) ---
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# --- Auth redirects (login/logout) ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'producto_list'
LOGOUT_REDIRECT_URL = 'login'

# --- Email (en dev, consola) ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- Seguridad mínima en dev ---
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# --- ID por defecto de clave primaria ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
