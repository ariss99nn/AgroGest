from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sale
from .serializers import SaleSerializer
from rest_framework.permissions import IsAuthenticated
from Usuario.permissions import IsAdminOrReadOnly  # Permiso personalizado que definiremos

class SaleListCreateAPIView(APIView):
    # Solo usuarios autenticados y con permiso IsAdminOrReadOnly pueden usar estas vistas
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request):
        # Obtener todas las ventas
        sales = Sale.objects.all()
        # Serializar las ventas para convertirlas a JSON
        serializer = SaleSerializer(sales, many=True)
        # Devolver la lista serializada como respuesta
        return Response(serializer.data)

    def post(self, request):
        # Recibir datos para crear una nueva venta
        serializer = SaleSerializer(data=request.data)
        # Validar los datos recibidos
        if serializer.is_valid():
            # Guardar la nueva venta si los datos son válidos
            serializer.save()
            # Responder con los datos creados y código 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si hay errores, responder con esos errores y código 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleRetrieveUpdateDestroyAPIView(APIView):
    # Mismos permisos para esta vista que para la lista/creación
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_object(self, pk):
        # Método para obtener una venta por su id (pk)
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return None

    def get(self, request, pk):
        # Obtener venta específica
        sale = self.get_object(pk)
        if not sale:
            # Si no existe, responder error 404
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        # Serializar la venta
        serializer = SaleSerializer(sale)
        # Responder con la venta serializada
        return Response(serializer.data)

    def put(self, request, pk):
        # Actualizar una venta específica
        sale = self.get_object(pk)
        if not sale:
            # Si no existe, error 404
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        # Serializar con datos nuevos para validación y actualización
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            # Guardar cambios si son válidos
            serializer.save()
            # Responder con datos actualizados
            return Response(serializer.data)
        # Si errores de validación, responder con error 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Eliminar una venta específica
        sale = self.get_object(pk)
        if not sale:
            # Error si no existe
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        # Eliminar la venta
        sale.delete()
        # Responder con código 204 (sin contenido)
        return Response(status=status.HTTP_204_NO_CONTENT)
