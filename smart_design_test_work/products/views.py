from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()

        # # Пример использования фильтрации через GET параметры
        # # Фильтр по названию товара .../?title=<value>
        # title = request.query_params.get('title')
        # if title:
        #     products = products.filter(title=title)
        # # Фильтр по какому-либо параметру .../?parameter__<name>=<value>
        # parameter = {k.split('__')[-1]: v for k, v in request.query_params.items() if 'parameter' in k}
        # if parameter:
        #     products = products.filter(parameters__contains=parameter)

        # Пример использования фильтрации через отправку JSON
        ids = request.data.get('ids')
        if ids:
            products = products.filter(id__in=ids)
        titles = request.data.get('titles')
        if titles:
            products = products.filter(title__in=titles)
        parameters = request.data.get('parameters')
        if parameters:
            for param in parameters:
                products = products.filter(parameters__contains=param)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        new_products = request.data.get('products')
        if new_products:
            prod_objects = self.__get_prod_objects(new_products)
            if prod_objects:
                Product.objects.bulk_create(prod_objects)
                return Response({'detail': 'OK'})
        return Response({'error': 'True','detail': 'Need correct data'})

    def __get_prod_objects(self, products):
        new_products = []
        for product in products:
            if product.get('title'):
                new_product = Product(**product)
                new_products.append(new_product)
            else:
                return False
        return new_products
