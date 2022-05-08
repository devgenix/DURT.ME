from django.contrib import admin

from django.urls import path, include
from django.urls import re_path as url

from django.conf import settings
from django.conf.urls.static import static

from API.views import Redirect, Shorten
from unauth.views import Shortener

urlpatterns = [

    path('', include('unauth.urls')),
    
    path('<str:url>', Redirect, name='redirect'),
    
    path('api/shorten', Shorten, name='shorten'),
    
    path('auth-api/shorten', Shortener, name='auth-shorten'),
    
    path('admin/', admin.site.urls),
    
    url(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
