
from django.urls import path
from . import views
from rest_framework import routers 
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewSet)
router.register('product-rating', views.ProductRatingViewSet)
router.register('store', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
router.register('vendors', views.VendorViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)
router.register('order-items', views.OrderItemsViewSet)
router.register('search', views.ProductSearchViewSet)
router.register('store-filter', views.ProductListByCategoryViewSet)

  
urlpatterns = [


    
    path('vendor-login', views.vendor_login),
    path('customer-login', views.customer_login),
    path('vendor-products/<int:vendor_id>', views.VendorProductsViewSet.as_view()),
    path('store/tags/<str:tag>', views.TagProductsList.as_view())
    
    # path('store-filter/', views.ProductListByCategory.as_view()),
    # path('product/<int:pk>', views.ProductDetail.as_view()),
    # path('categories/', views.CategoryList.as_view()),
    # path('category/<int:pk>', views.CategoryDetail.as_view()),
    # path('customers/', views.CustomerList.as_view()),
    # path('customer/<int:pk>', views.CustomerDetail.as_view()),
    # path('orders/', views.OrderList.as_view()),
    # path('order/<int:pk>', views.OrderDetail.as_view()),
    # path('order-items/', views.OrderItemsList.as_view()),
    # path('order-item/<int:pk>', views.OrderItemsDetail.as_view()),
    # path('search/', views.ProductSearchList.as_view()),

]
 
urlpatterns += router.urls
