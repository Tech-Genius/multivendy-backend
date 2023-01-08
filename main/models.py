from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# vendor

class Vendor(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)

# 
    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.phone   

    class Meta:
        verbose_name_plural = "1: Vendors"       
    


#Product category
class ProductCategory(models.Model):
    title = models.CharField(max_length=225)
    details = models.TextField(null = True)
    image = models.ImageField(upload_to='category-images', null=True) 
    slug = models.SlugField(null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2: Product Categories"     

#products
class Products(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='category_products', null=True, on_delete=models.CASCADE )
    vendor= models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(default="detail")
    price = models.FloatField()
    tags = models.TextField(default="tags")
    image = models.ImageField(upload_to='store-images', null=True)
    date_added = models.DateTimeField(auto_now_add=True, null = True)
    featured_image1 = models.ImageField(upload_to='featured-images', null=True,blank=True)
    featured_image2 = models.ImageField(upload_to='featured-images', null=True,blank=True)
    featured_image3 = models.ImageField(upload_to='featured-images', null=True, blank=True)
    featured_image4 = models.ImageField(upload_to='featured-images', null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
       ordering = ['date_added'] 

    def tag_list (self):
        tagList =self.tags.split(',')
        return tagList  

    class Meta:
        verbose_name_plural = "3: Products" 


#customer
class Customer(models.Model):
    first_name= models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    
    def __str__(self):
        if self.first_name:
           return self.first_name
        else:
            return self.phone

    class Meta:
        verbose_name_plural = "4: Customers"       

#order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.order_time)

    class Meta:
        verbose_name_plural = "5: Orders" 


#orderitems
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name ='order_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
 
    class Meta:
        verbose_name_plural = "6: Order Items"


#customer address
class CustomerAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='customer_addresses')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "7: Customer Addresses"       

#rating and reviews

class ProductRating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='rating_customer')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_rating')
    rating = models.IntegerField()
    reviews = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.rating} - {self.reviews}'

    class Meta:
        verbose_name_plural = "8: Product Ratings"