from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ('product', 'quantity', 'price',)


class StockSerializer(serializers.ModelSerializer):

    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        exclude = ('products',)

    # настройте сериализатор для склада

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            position['stock_id'] = stock.id
            StockProduct.objects.create(**position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            position['stock_id'] = stock.id
            position['product_id'] = position['product'].id
            del position['product']

            StockProduct.objects.filter(
                product_id=position.get('product_id'),
                stock_id=position.get('stock_id')
            ).update_or_create(
                defaults={
                    'price': position.get('price'),
                    'quantity': position.get('quantity'),
                    'product_id': position.get('product_id'),
                    'stock_id': position.get('stock_id'),
                }
            )

        return stock
