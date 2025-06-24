from rest_framework.views import APIView                     # Clase base para vistas API
from rest_framework.response import Response                 # Para retornar respuestas HTTP en formato JSON
from rest_framework import status                            # Módulo para códigos de estado HTTP
from django.http import Http404                              # Excepción 404 personalizada
from .models import SoilAnalysis                             # Importa el modelo SoilAnalysis
from .serializers import SoilAnalysisSerializer              # Importa el serializador para SoilAnalysis

class SoilAnalysisListCreateAPIView(APIView):
    """
    GET: Lista todos los análisis de suelo.
    POST: Crea un nuevo análisis de suelo.
    """

    def get(self, request):
        analyses = SoilAnalysis.objects.all()                              # Obtiene todos los registros
        serializer = SoilAnalysisSerializer(analyses, many=True)           # Serializa en lista
        return Response(serializer.data, status=status.HTTP_200_OK)        # Devuelve los datos serializados

    def post(self, request):
        serializer = SoilAnalysisSerializer(data=request.data)             # Deserializa los datos recibidos
        if serializer.is_valid():                                          # Verifica si son válidos
            serializer.save()                                              # Guarda en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SoilAnalysisRetrieveUpdateDestroyAPIView(APIView):
    """
    GET: Obtiene un análisis por ID.
    PUT: Actualiza un análisis por ID.
    DELETE: Elimina un análisis por ID.
    """

    def get_object(self, pk):
        try:
            return SoilAnalysis.objects.get(pk=pk)                         # Intenta recuperar el objeto
        except SoilAnalysis.DoesNotExist:
            raise Http404("Soil Analysis not found")                       # Lanza error 404 si no existe

    def get(self, request, pk):
        analysis = self.get_object(pk)                                     # Recupera el objeto
        serializer = SoilAnalysisSerializer(analysis)                      # Serializa el objeto
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        analysis = self.get_object(pk)
        serializer = SoilAnalysisSerializer(analysis, data=request.data)   # Carga los nuevos datos
        if serializer.is_valid():                                          # Valida los datos
            serializer.save()                                              # Guarda si son válidos
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        analysis = self.get_object(pk)
        analysis.delete()                                                  # Elimina el objeto
        return Response(status=status.HTTP_204_NO_CONTENT)                # Retorna respuesta vacía
