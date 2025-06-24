from rest_framework.views import APIView                     # Vista base para APIView
from rest_framework.response import Response                 # Clase para retornar respuestas JSON
from rest_framework import status                            # Códigos de estado HTTP
from django.http import Http404                              # Excepción para objetos no encontrados
from .models import Product                                   # Modelo Product
from .serializers import ProductSerializer                   # Serializador para el modelo Product
class ProductListCreateAPIView(APIView):
    """
    GET: Lista todos los productos.
    POST: Crea un nuevo producto.
    """

    def get(self, request):
        products = Product.objects.all()                                      # Obtiene todos los productos
        serializer = ProductSerializer(products, many=True)                  # Serializa todos los productos
        return Response(serializer.data, status=status.HTTP_200_OK)          # Retorna respuesta exitosa

    def post(self, request):
        serializer = ProductSerializer(data=request.data)                    # Deserializa datos de entrada
        if serializer.is_valid():
            serializer.save()                                                # Guarda si es válido
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna con 201 Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Errores de validación

class ProductRetrieveUpdateDestroyAPIView(APIView):
    """
    GET: Obtiene un producto.
    PUT: Actualiza un producto.
    DELETE: Elimina un producto.
    """

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)              # Intenta obtener el producto
        except Product.DoesNotExist:
            raise Http404("Product not found")             # Lanza 404 si no existe

    def get(self, request, pk):
        product = self.get_object(pk)                      # Obtiene el producto
        serializer = ProductSerializer(product)            # Lo serializa
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)                      # Obtiene el producto
        serializer = ProductSerializer(product, data=request.data)  # Lo deserializa con nuevos datos
        if serializer.is_valid():
            serializer.save()                              # Guarda si es válido
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)                      # Obtiene el producto
        product.delete()                                   # Elimina el producto
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna 204 (sin contenido)