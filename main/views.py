from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import generics,permissions, pagination, viewsets
from . import serializers
from . import models
from . models import Products
from rest_framework import filters
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



class VendorViewSet(viewsets.ModelViewSet):
    queryset = models.Vendor.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.VendorDetailSerializer
        return serializers.VendorSerializer    
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def vendor_login(request):
    if request.method == 'POST':

       email = request.POST['email']
       password = request.POST['password']
       vendorData = models.Vendor.objects.get(email=email, password=password)
       if vendorData:
          return JsonResponse({'bool': True})
       else:
          return JsonResponse({'bool': False})  


# all product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all().order_by('-date_added')
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ProductDetailSerializer
        return serializers.ProductListSerializer 


# specific vendor course

class VendorProductsViewSet(generics.ListAPIView):
    serializer_class = serializers.ProductListSerializer
    def get_queryset(self):
        vendor_id = self.kwargs['vendor_id']
        vendor = models.Vendor.objects.get(pk=vendor_id)
        return models.Vendor.objects.filter(password=vendor)




# related product
class RelatedProductList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        product_id = self.kwargs['pk']
        product = models.Products.objects.get(id = product_id)
        qs = qs.filter(category=product.category).exclude(id=product_id)
        return qs






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
        qs = qs.filter(category=category).order_by('-date_added')
        return qs



#tags
class TagProductsList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductListSerializer
    pagination_class= pagination.PageNumberPagination
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs['tag']
        qs = qs.filter(tags__icontains=tag).order_by('-date_added')
        return qs



#search
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
@csrf_exempt
def customer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        customerData = models.Customer.objects.get(email=email, password=password)
        if customerData:
            return JsonResponse({'bool':True})
        else:
            return JsonResponse({'bool': False})    



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

