from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    other_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk')

    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'other_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)


    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        return obj.get_discount()
