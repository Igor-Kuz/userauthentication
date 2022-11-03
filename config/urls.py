from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from django.shortcuts import render

def auth(request):
    return render(request, 'auth.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('src.routes')),
    path('', include('src.oauth.urls')),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', auth)

]
