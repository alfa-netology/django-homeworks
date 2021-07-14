from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockProductViewSet(ModelViewSet):
    queryset = StockProduct.objects.all()
    serializer_class = ProductPositionSerializer
