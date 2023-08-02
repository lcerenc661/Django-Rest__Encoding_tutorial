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
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'other_url',
            'email',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]
     # Create method

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # # update method
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)
    

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
