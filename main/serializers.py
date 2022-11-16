from pyexpat import model
from rest_framework import serializers
from . import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['user', 'address'] 


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']         
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = ['id','category', 'vendor', 'title', 'price','image', 'date_added']         


class ProductDetailSerializer(serializers.ModelSerializer):
    product_rating = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Products
        fields = ['id','category', 'vendor', 'image', 'title', 'detail', 'price', 'product_rating', 'featured_image1', 'featured_image2', 'featured_image3', 'featured_image4']         
    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1


class ProductListByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = ['id','category', 'vendor', 'title', 'price','image', 'date_added']         




class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ['id','title','image']         


class CategoryDetailSerializer(serializers.ModelSerializer):
    # Category_rating = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.ProductCategory
        fields = ['id','title', 'detail']         
    def __init__(self, *args, **kwargs):
        super(CategoryDetailSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1

        

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'phone']         


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'phone']         
    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['customer','order_time']         


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['customer','order_time']         
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1


class OrderItemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['order','product']         


class OrderItemsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['order','product']         
    def __init__(self, *args, **kwargs):
        super(OrderItemsDetailSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id','customer', 'address', 'default_address']         
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ['id','customer', 'product', 'rating', 'reviews', 'added_time']         
    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer, self).__init__ (*args, **kwargs)
        self.Meta.depth = 1
