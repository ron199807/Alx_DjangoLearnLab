from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet, CartViewSet, CartItemViewSet, paymentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r"product", ProductViewSet)
router.register(r"order", OrderViewSet)
router.register(r"cart", CartViewSet)
router.register(r"cart-items", CartItemViewSet)
router.register(r"payment", paymentViewSet)

urlspatterns = [
    path('api/', include(router.urls)),
]
