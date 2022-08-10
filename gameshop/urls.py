"""gameshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

from apps.users.views import LoginUserAPIView, UserRegistrationAPIView
from apps.store.views import GameAPIList, GameAPIUpdate, GenreViewSet
from apps.orders.views import CreateOrder


router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet, basename='genre')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/registration/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('api/v1/login/', LoginUserAPIView.as_view(), name='user_login'),
    path('api/v1/orders/', CreateOrder.as_view(), name='create_order'),
    path('api/v1/games/', GameAPIList.as_view(), name='games_list'),
    path('api/v1/games/<int:pk>/', GameAPIUpdate.as_view(), name='game'),
    path('api/v1/', include(router.urls)),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)