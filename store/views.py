
# store/views.py

from rest_framework import generics
from .models import Category, Product, CartItem
# store/views.py
from store import Serializers
# store/views.py
from rest_framework.permissions import IsAuthenticated
from Users.permission import productmanager,cartmanager


# List and Detail views for Category
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Serializers.CategorySerializer
    permission_classes= [productmanager|cartmanager]

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = Serializers.ProductSerializer
    lookup_field = "slug"

# List and Detail views for Product
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class =Serializers.ProductSerializer[cartmanager|productmanager]

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = Serializers.ProductSerializer
    lookup_field = "slug"

# List and Create views for Cart
class CartItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = Serializers.CartItemSerializer[cartmanager]

class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = Serializers.CartItemSerializer
