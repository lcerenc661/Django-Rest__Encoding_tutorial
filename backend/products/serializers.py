from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from products.validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer, ProductInlineSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(
    #     source='user.product_set.all', read_only=True, many=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    other_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk')
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello,
                                              unique_product_title])
    name = serializers.CharField(source='title', read_only=True)
    body = serializers.CharField(source='content')

    class Meta:
        model = Product
        fields = [
            'owner',
            # 'related_products',
            'url',
            'edit_url',
            'other_url',
            # 'email',
            'pk',
            'title',
            'name',
            'body',
            'price',
            'sale_price',
        ]

    def get_my_user_data(self, obj):
        if obj.user is None:
            return None
        return {
            "username": obj.user.username
        }


    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     queryset = Product.objects.filter(user=user, title__iexact=value)
    #     if queryset.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already a product name.")
    #     return value

    # # Create method

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

    # def get_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     return obj.get_discount()
