
from django.shortcuts import render
from rest_framework import generics,permissions, pagination, viewsets
from . import serializers
from . import models
from . models import Products
from rest_framework import filters
# Create your views here.



class VendorViewSet(viewsets.ModelViewSet):
    queryset = models.Vendor.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.VendorDetailSerializer
        return serializers.VendorSerializer    
    # permission_classes = [permissions.IsAuthenticated]



class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all().order_by('-date_added')
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ProductDetailSerializer
        return serializers.ProductListSerializer 



class RelatedProductDetailViewSet(generics.ListAPIView):
    serializer_class = serializers.ProductDetailSerializer
    def get_queryset(self):
        return models.Products.objects.filter(category__id=self.kwargs['category__id'])






    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     category = self.request.GET['category']
    #     category = models.ProductCategory.objects.get(id=category)
    #     qs = qs.filter(category=category)
        # return qs


class ProductListByCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductListByCategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET['category']
        category = models.ProductCategory.objects.get(id=category)
        qs = qs.filter(category=category)
        return qs



class ProductSearchViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    search_fields = ['title', 'category__title']
    filter_backends = (filters.SearchFilter,)
    qs = Products.objects.all()
    serializer_class = serializers.ProductListSerializer  







class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductCategory.objects.all() 
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.CategoryDetailSerializer
        return serializers.CategoryListSerializer    

    # permission_classes = [permissions.IsAuthenticated]



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.CustomerDetailSerializer
        return serializers.CustomerListSerializer    

    # permission_classes = [permissions.IsAuthenticated]



class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListSerializer
    pagination_class = pagination.LimitOffsetPagination
    # permission_classes = [permissions.IsAuthenticated]


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     # queryset = models.Order.objects.all()
#     serializer_class = serializers.OrderDetailSerializer
#     def get_queryset(self):
#         order_id = self.kwargs['pk']
#         order = models.Order.objects.get(id=order_id)
#         order_items = models.OrderItems.objects.filter(order=order)
#         return order


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemsListSerializer
     

class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerAddressSerializer
    queryset = models.CustomerAddress.objects.all()


class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductRatingSerializer
    queryset = models.ProductRating.objects.all()

