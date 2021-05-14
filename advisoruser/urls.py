"""advisoruser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import reverse
from testapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',views.AdvisorCRUDCBV)
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'^auth-jwt/', obtain_jwt_token),
     url(r'^auth-jwt-refresh/', refresh_jwt_token),
     url(r'^auth-jwt-verify/', verify_jwt_token),s
]
