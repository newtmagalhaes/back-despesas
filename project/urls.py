"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from drf_spectacular import views

urlpatterns = [
    # OpenAPI 3
    path('api/schema/', views.SpectacularAPIView.as_view(), name='api_schema'),
    path('api/swagger/', views.SpectacularSwaggerView.as_view(url_name='api_schema'), name='swagger'),
    path('api/redoc/', views.SpectacularRedocView.as_view(url_name='api_schema'), name='redoc'),

    path('api/', include('api.views')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
