
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# vendor

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

# 
    def __str__(self):
        return self.user.username
    


#Product category
class ProductCategory(models.Model):
    title = models.CharField(max_length=225)
    details = models.TextField(null = True)
    image = models.ImageField(upload_to='category-images', null=True) 
    slug = models.SlugField(null=True)


    def __str__(self):
        return self.title

#products
class Products(models.Model):
    category = models.ManyToManyField(ProductCategory, related_name='category_products' )
    vendor= models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='store-images', null=True)
    date_added = models.DateTimeField(auto_now_add=True, null = True)
    featured_image1 = models.ImageField(upload_to='featured-images', null=True, blank=True)
    featured_image2 = models.ImageField(upload_to='featured-images', null=True, blank=True)
    featured_image3 = models.ImageField(upload_to='featured-images', null=True, blank=True)
    featured_image4 = models.ImageField(upload_to='featured-images', null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
       ordering = ['date_added'] 
        


#customer
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

#order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.order_time)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name ='order_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
 
#customer address
class CustomerAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='customer_addresses')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address

#rating and reviews

class ProductRating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='rating_customer')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_rating')
    rating = models.IntegerField()
    reviews = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.rating} - {self.reviews}'