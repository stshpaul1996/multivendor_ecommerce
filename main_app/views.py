from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from . import serializers
from . import models


# Vender create and list view
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Vender retrieve update destroy view
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer

# Category create and list view
class CategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


# Category retrieve update destroy view
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    

#Product create list view
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    

#Product retrieve update destroy view
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer


#Customer create list view
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
  

#Customer retrieve update destroy view
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    

#Order list create view
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    

#Order retrieve view
class OrderDetail(generics.ListAPIView):
    #queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemsSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        try:
            order = models.Order.objects.get(id = order_id)
            order_items = models.OrderItems.objects.filter(order=order)
            return order_items
        except:
            return super().get_queryset()


#Customer address view
class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerAddressSerializer
    queryset = models.CustomerAddress.objects.all()


#Prodcut rating view
class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductRatingSerializer
    queryset = models.ProductRating.objects.all() 

    # def get_queryset(self):
    #     product_id = self.kwargs['pk']
    #     product = models.Product.objects.get(id=product_id)
    #     rating = models.ProductRating.objects.filter(product=product)
    #     return rating 

