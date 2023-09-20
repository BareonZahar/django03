"""
URL configuration for django03 project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from anketa import views
from django03 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('forma/1', views.forma1,name='forma1'),
    path('forma/2', views.forma2,name='forma2'),
    path('forma/3', views.forma3, name='forma3'),
    path('forma/upload', views.upload,name= 'upload'),
    # path('fo2/',views.forma2,name='fo2')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
