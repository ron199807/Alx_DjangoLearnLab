from rest_framework import serializers
from .models import Category, Product, Order, OrderItems, Cart, CartItem, payment

# category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


# product serializer 
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) # to display category details

    class Meta:
        model = Product
        fields= ['id','name', 'description', 'prices', 'stock', 'available', 'category']

# orderItem serializer
class OrderItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True) # to display product details in the order

    class Meta:
        model = OrderItems
        fields = ['id', 'product', 'quantity', 'price']


# order serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True, read_only=True) # to display all items in the order

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'updated_at', 'total_price', 'is_paid', 'items']


# cartitem serializer
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True) # to display product details

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantinty']


# cart serializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True) # to display all items in the cart

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']


# payment serializer
class paymentSerializer(serializers.ModelSerializer):
    model = payment
    fields = ['id', 'order', 'amount', 'payment_method', 'timestamp']

