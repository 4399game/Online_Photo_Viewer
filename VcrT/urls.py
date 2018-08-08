"""VcrT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static

# Import
# here that import you module
from . import settings

urlpatterns = [

    # here that admin url
    path('admin/', admin.site.urls),

    # here that vcr site urls
    path('メリー/', include('vcr_apps.user.urls') ),
    path('する/', include('vcr_apps.option.urls') ),
    path('けんじゃた/', include('vcr_apps.kuukann.urls') ),
    path('', include('vcr_apps.web.urls') ),

    # here that util urls
    path('search/', include('haystack.urls')),
]

# make static can be use ~

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)