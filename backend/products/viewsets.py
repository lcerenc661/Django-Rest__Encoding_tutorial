from rest_framework import viewsets, mixins

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrive -> Product instance Detail View
    post -> Create -> New Instance
    put -> update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default

class ProductGenericViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin
        ):
    '''
    get -> list -> Queryset
    get -> retrive -> Product instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default
    