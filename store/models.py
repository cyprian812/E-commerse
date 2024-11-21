from django.db import models
from django.utils.text import slugify

# Create your models here.
# store/models.py

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)# with a maximum length of 100 characters to store the name of the category.
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name #The string representation of a Category instance

    def get_absolute_url(self):
        return reverse("store:category_detail", kwargs={"slug": self.slug})#models to provide a standard way of determining the URL of an object. In this case, it returns the URL for viewing the details of the category.

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)# A unique URL-friendly identifier for the product.
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_of_product=models.CharField(max_length=150, default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name #method returns the product's name as a string representation.

    def get_absolute_url(self):
        return reverse("store:product_detail", kwargs={"slug": self.slug})#enerate a URL from the name of a URL pattern, which helps avoid hardcoding URLs in your views and templates.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    product_name=models.CharField(max_length=150,default=True)#This model uses a foreign key to link to the Product model, stores the quantity of the product in the cart, tracks when the item was added, and keeps the product's name in a string field.
