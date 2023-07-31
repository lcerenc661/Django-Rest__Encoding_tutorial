# import json

# from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

# from products.models import Product
from products.serializers import ProductSerializer

# GET METHOD
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API Vie
#     """
#     instance = Product.objects.all().order_by("?").first()
#     print(instance)
#     data = {}
#     if instance:
#         # data = model_to_dict(
#         #     instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#         print(data)
#         # serialization -> models instance (model_data)

#     return Response(data)


# POST METHOD
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API Vie
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid": 'not good data'}, status=400)
