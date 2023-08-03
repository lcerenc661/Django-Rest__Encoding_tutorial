from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from search import client


# class SearchListView(generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         query = request.GET.get('q')
#         tag = request.GET.get('tag') or None
#         if not query:
#             return Response('', status=400)
#         results = client.perfom_search(query, tags=tag)
#         return Response(results)


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
