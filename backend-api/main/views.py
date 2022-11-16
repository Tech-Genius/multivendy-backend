
from django.shortcuts import render
from rest_framework import generics,permissions, pagination, viewsets
from . import serializers
from . import models
from . models import Products
from rest_framework import filters
# Create your views here.



class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all().order_by('-date_added')[:6]
    serializer_class = serializers.ProductListSerializer  

    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     category = self.request.GET['category']
    #     category = models.ProductCategory.objects.get(id=category)
    #     qs = qs.filter(category=category)
        # return qs

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    # related_product = Products.objects.filter(category__in=product.category.all()).exclude(slug=slug).distinct()[:3]
    serializer_class = serializers.ProductDetailSerializer

    # permission_classes = [permissions.IsAuthenticated]

class ProductListByCategory(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductListByCategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET['category']
        category = models.ProductCategory.objects.get(id=category)
        qs = qs.filter(category=category)
        return qs



class ProductSearchList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    search_fields = ['title', 'category__title']
    filter_backends = (filters.SearchFilter,)
    qs = Products.objects.all()
    serializer_class = serializers.ProductListSerializer  







class CategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    
    serializer_class = serializers.CategoryListSerializer
    # permission_classes = [permissions.IsAuthenticated]



class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategoryDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]





class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerListSerializer
    # permission_classes = [permissions.IsAuthenticated]



class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListSerializer
    pagination_class = pagination.LimitOffsetPagination
    # permission_classes = [permissions.IsAuthenticated]



class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     # queryset = models.Order.objects.all()
#     serializer_class = serializers.OrderDetailSerializer
#     def get_queryset(self):
#         order_id = self.kwargs['pk']
#         order = models.Order.objects.get(id=order_id)
#         order_items = models.OrderItems.objects.filter(order=order)
#         return order


class OrderItemsList(generics.ListCreateAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemsListSerializer
     



class OrderItemsDetail(generics.ListAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemsDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerAddressSerializer
    queryset = models.CustomerAddress.objects.all()




class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductRatingSerializer
    queryset = models.ProductRating.objects.all()

