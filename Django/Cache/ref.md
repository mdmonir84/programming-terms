# Django cache Framework

## memcached
### Installation 
- pip3 install python-memcached

### Update settings.py file.

```
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1;11211',
    }
}
```

## Database Cache
## Local-Memory Cache

### Update settings.py file.

```
# We can skip the location part if we require only one portion to store cache and 
# if we want to distinguish between caches then we should use LOCATION.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'Dashboard',
		'TIMEOUT': 500,
		'OPTIONS':{
			'MAX_ENTRIES': 10,
			'CULL_FREQUENCY': 1,
		}
    }
}
```
## Cache args/parameters

- TIMEOUT

  - This argument takes time in seconds. It is similar to expire time for cookies. You can also define the expire time of cache data.
By default, its 5 minutes or 300 seconds.

- OPTIONS

  - This key is set for a particular option concerning that particular backend engine. It will have values for that backend.
 There are different options for Memcached and Local Memory Cache.

  - These options are valid for local memory, database, and file-system caching implementations.

  - You can define different options in custom cache engines as this field gives superior control over your cache data.

  - These are some general options:

    - MAX_ENTRIES
      - This argument takes in the maximum number of cache items that can be stored. Here the developer defines a capacity for the database, when capacity is filled.
      The server will culminate the previous entries.

    - CULL_FREQUENCY
    - This sets up the frequency of deletion of cookies when the maximum number of entries has reached. This argument will take integer parameters as well.

    - For example – You have given 2 as a value of CULL_FREQUENCY. 
  When the MAX_ENTRIES is reached, the entries will be cut in half, like Thanos Snap and half of the entries are deleted.

### Implementation of Options in Database

### KEY_PREFIX

### VERSION

### KEY_FUNCTION

## Implementing Caching in Django

### Per-site Caching Implementation

### Update settings.py (Order is very important)

```
MIDDLEWARE =[
			'django.middleware.security.SecurityMiddleware',
			'django.contrib.sessions.middleware.SessionMiddleware',


			#Dashboard #Caching Middleware
			'django.middleware.cache.UpdateCacheMiddleware',
			'django.middleware.common.CommonMiddleware',
			'django.middleware.cache.FetchFromCacheMiddleware',
			
]

# Key in `CACHES` dict
CACHE_MIDDLEWARE_ALIAS = 'default'

# Additional prefix for cache keys
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Cache key TTL in seconds
CACHE_MIDDLEWARE_SECONDS = 600
```

### Per-View Caching Implementation

```
#Dashboard webapp/views.py
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(200)
def index(request):
	return HttpResponse('<h1> Django Cache Framework Tutorial</h1>')



#Dashboard webapp/urls.py
from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(300)views.home, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('mem/', views.mem, name='mem'),
]
```
### Template fragment caching
```
{% load cache %}
{% cache 500 sidebar %}
    .. sidebar ..
{% endcache %}
```
### cache update during Database Model update

```
from django.core.cache import cache

class ArticlesListView(ListView):

    ...

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors_count = cache.get('authors_count')
        if authors_count is None:
            authors_count = Author.objects.count()
            cache.set('authors_count', authors_count)
        context['authors_count'] = authors_count
        ...
        return context

```
Ref:  
- https://dizballanze.com/django-project-optimization-part-3/
- https://testdriven.io/blog/django-caching/


