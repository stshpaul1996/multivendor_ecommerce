from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewSet)
router.register('rating', views.ProductRatingViewSet)


urlpatterns = [
    #vendor
    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>/', views.VendorDetail.as_view()),
    #products
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/',views.ProductDetail.as_view()),
    #product categories
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/',views.CategoryDetail.as_view()),
    #customers
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/',views.CustomerDetail.as_view()),
    #orders
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/',views.OrderDetail.as_view()),
]+router.urls