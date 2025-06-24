from rest_framework.views import APIView                     # Clase base para vistas API
from rest_framework.response import Response                 # Para retornar respuestas JSON
from rest_framework import status                            # Códigos de estado HTTP
from django.http import Http404                              # Excepción para manejar 404
from .models import Sowing                                   # Importa el modelo Sowing
from .serializers import SowingSerializer                    # Importa el serializador de Sowing

class SowingListCreateAPIView(APIView):
    """
    GET: Lista todas las siembras.
    POST: Crea una nueva siembra.
    """

    def get(self, request):
        sowings = Sowing.objects.all()                                      # Obtiene todas las siembras
        serializer = SowingSerializer(sowings, many=True)                  # Serializa el queryset
        return Response(serializer.data, status=status.HTTP_200_OK)        # Retorna la lista con 200 OK

    def post(self, request):
        serializer = SowingSerializer(data=request.data)                   # Deserializa los datos recibidos
        if serializer.is_valid():
            serializer.save()                                              # Guarda si los datos son válidos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SowingRetrieveUpdateDestroyAPIView(APIView):
    """
    GET: Obtener una siembra.
    PUT: Actualizar una siembra.
    DELETE: Eliminar una siembra.
    """

    def get_object(self, pk):
        try:
            return Sowing.objects.get(pk=pk)               # Intenta obtener la siembra por ID
        except Sowing.DoesNotExist:
            raise Http404("Sowing not found")              # Lanza 404 si no existe

    def get(self, request, pk):
        sowing = self.get_object(pk)                       # Obtiene la siembra
        serializer = SowingSerializer(sowing)              # La serializa
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        sowing = self.get_object(pk)                       # Obtiene la siembra
        serializer = SowingSerializer(sowing, data=request.data)  # Carga los nuevos datos
        if serializer.is_valid():
            serializer.save()                              # Guarda si es válido
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sowing = self.get_object(pk)                       # Obtiene la siembra
        sowing.delete()                                    # La elimina
        return Response(status=status.HTTP_204_NO_CONTENT) # Retorna 204 (sin contenido)
