"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from store.views import CategoryListView, CategoryDetailView, ProductDetailView, CartView, AddToCartView
# from django.urls import path, include
# app_name = "store"

# urlpatterns =  [
#     path('admin/', admin.site.urls),
#     # store/urls.py 
#     path("", CategoryListView.as_view(), name="category_list"),
#     path("category/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
#     path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
#     path("cart/", CartView.as_view(), name="cart"),
#     path("add-to-cart/<int:pk>/", AddToCartView.as_view(), name="add_to_cart"),   
# #adnin
# #     path('', include('store.urls', namespace='store')),
# ]
# store/urls.py
from  django.urls import path, include
from django.urls import path
# from store.views import CartItemDetailAPIView,CartItemListCreateAPIView,CategoryDetailAPIView,CategoryListAPIView,ProductListAPIView,ProductDetailAPIView,
from store.views import CartItemDetailAPIView, CartItemListCreateAPIView, CategoryDetailAPIView, CategoryListAPIView, ProductListAPIView, ProductDetailAPIView
from Users.views import CustomRegisterView

app_name = "store"

urlpatterns = [
    
    # # API views
    path("api/categories/", CategoryListAPIView.as_view(), name="api_category_list"),
    path("api/categories/<slug:slug>/", CategoryDetailAPIView.as_view(), name="api_category_detail"),
    path("api/products/", ProductListAPIView.as_view(), name="api_product_list"),
    path("api/products/<slug:slug>/", ProductDetailAPIView.as_view(), name="api_product_detail"),
    path("api/cart/", CartItemListCreateAPIView.as_view(), name="api_cart_list"),
    path("api/cart/<int:pk>/", CartItemDetailAPIView.as_view(), name="api_cart_detail"),

#
 path("auth", include('django.contrib.auth.urls')),
    path("api/auth/", include('dj_rest_auth.urls')),
    path("api/auth/registration/", include('dj_rest_auth.registration.urls')),
    path("auth/signup/", CustomRegisterView.as_view()),
    
            # ]
            # api/categories/ [name='api_category_list']
            # api/categories/<slug:slug>/ [name='api_category_detail']
            # api/products/ [name='api_product_list']
            # api/products/<slug:slug>/ [name='api_product_detail']
            # api/cart/ [name='api_cart_list']
            # api/cart/<int:pk>/ [name='api_cart_detail']
            # auth
            # api/auth/
            # api/auth/registration/
            # auth/signup/


]
