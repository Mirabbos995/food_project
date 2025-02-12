"""
URL configuration for food project.

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
from django.urls import path, re_path,include



from ovqat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/createfood/', Createfood.as_view()),
    path('api/v1/getfood/', Listfood.as_view()),
    path('api/v1/updatefood/<int:pk>/', Updatefood.as_view()),
    path('api/v1/deletefood/<int:pk>/', Deletefood.as_view()),
    path('api/v1/createcategory/', Createcategory.as_view()),
    path('api/v1/getcategory/', Listcategory.as_view()),
    path('api/v1/updatecategory/<int:pk>/', Updatecategory.as_view()),
    path('api/v1/deletecategory/<int:pk>/', Deletecategory.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]