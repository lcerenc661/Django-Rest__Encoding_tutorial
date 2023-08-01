from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        return obj.get_discount()
