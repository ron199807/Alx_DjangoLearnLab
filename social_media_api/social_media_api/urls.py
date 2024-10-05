"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/', include('accounts.urls')),

   # swagger docs
   from django.urls import path, re_path

urlpatterns = [
    # Your other URL patterns
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

]



schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version='v1',
        description="API documentation for the Social Media application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@socialmedia.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



