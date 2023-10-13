"""
URL configuration for ecommerce project.

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
from django.urls import path
from shop import views
app_name="shop"

urlpatterns = [
    path('',views.allprodcat,name="allprodcat"),
    path('allproducts/<c>',views.allproducts,name="allproducts"),
    path('productdetails/<p>',views.productdetails,name="productdetails"),
    path('signup',views.user_signup,name="user_signup"),
    path('login',views.user_login,name="user_login"),
    path('logout',views.user_logout,name="user_logout"),
]
