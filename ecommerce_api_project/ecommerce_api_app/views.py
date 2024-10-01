from django.shortcuts import render

from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorator import action
from .models import Category, Product, Order, OrderItems, Cart, CartItem, payment
from .serializers import (
    CategorySerializer, ProductSerializer, OrderSerializer, CartSerializer, CartItemSerializer, paymentSerializer
)

# category viewset
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] # allows anyone to view the categories

# product viewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] # any one can view products

# Order viewset (for authenticated users only)
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perfom_create(self, serializer):
        serializer.save(user=self.request.user) # associate order with the logged-in user

# cart viewset (for authenticated users)
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perfom_create(self, serializer):
        serializer.save(user=self.request.user) # associate order with the logged-in user

# Cartitem viewset
class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def perfom_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart=cart)

# payment viewset (custom action on order viewsset)
class paymentViewSet(viewsets.ModelViewSet):
    serializer_class = paymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return
payment.objects.filter(order__user=self.request.user)

    def perfom_create(self, serializer):
        # payment processing logic to be expanded with actual payment integration
        serializer.save()


