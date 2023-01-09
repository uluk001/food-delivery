"""food_delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from apps.core.views import (BaseView, ProductListView, aboutUs, addCart, cart,
                             order, product, removeCart, search)

urlpatterns = [
    path('', ProductListView.as_view(), name='base'),
    path('test', BaseView.as_view(extra_context={'title': 'Food delivery'}), name='test'),
    path('product/<int:id>', product, name='product'),
    path('addCart<int:pk>', addCart, name='addCart'),
    path('cart/', cart, name='cart'),
    path('removeCart/<int:id>', removeCart, name='removeCart'),
    path('aboutUs', aboutUs, name='aboutUs'),
    path('search', search, name="search"),
    path('order', order, name='order')
]
