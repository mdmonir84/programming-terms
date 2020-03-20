# Build a Modern Web Application with Django and React on Ubuntu 18.04

Some tools that you can use when building more complex applications include:

- React, a JavaScript framework that allows developers to build web and native frontends for their REST API backends.
- Django, a free and open-source Python web framework that follows the model view controller (MVC) software architectural pattern.
- Django REST framework, a powerful and flexible toolkit for building REST APIs in Django.

## Installation

- Django: The web framework for the project.
- Django REST framework: A third-party application that builds REST APIs with Django.
- django-cors-headers: A package that enables CORS.

> pip install django djangorestframework django-cors-headers

Here is the coplete project tree

```
├── djangoreactproject
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```

Here is the settings.py
```
# ~/djangoreactproject/djangoreactproject/settings.py

...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',               # ADD
    'corsheaders'                   # ADD
]

MIDDLEWARE = [
...
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
'corsheaders.middleware.CorsMiddleware'           # ADD
]

...
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
       'localhost:3000',
)
...

```
Next, you can enable CORS. The CORS_ORIGIN_ALLOW_ALL setting specifies whether or not you want to allow CORS for all domains, and CORS_ORIGIN_WHITELIST is a Python tuple that contains allowed URLs.

In our case, because the React development server will be running at ```http://localhost:3000```, we will add new ```CORS_ORIGIN_ALLOW_ALL = False``` and CORS_ORIGIN_WHITELIST('localhost:3000',) settings to our settings.py file. Add these settings anywhere in the file:
