from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import CropMonitoring
from .serializers import CropMonitoring_Serializer


#CLASE QUE LISTA Y CREA MONITOREOS
class CropMonitoring_List_View(APIView):
    # GET: Lista todos los registros de monitoreo de cultivos
    def get(self, request):
        monitorings = CropMonitoring.objects.all()
        serializer = CropMonitoring_Serializer(monitorings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Crea un nuevo monitoreo
    def post(self, request):
        serializer = CropMonitoring_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#CLASE QUE DETALLE Y ACTUALIZA MONITOREOS
class CropMonitoring_Detail_View(APIView):
    # Método auxiliar para obtener un objeto o lanzar 404 si no existe
    def get_object(self, pk):
        try:
            return CropMonitoring.objects.get(pk=pk)
        except CropMonitoring.DoesNotExist:
            raise Http404("Crop Monitoring not found")

    # GET: Obtener detalle de un monitoreo
    def get(self, request, pk):
        monitoring = self.get_object(pk)
        serializer = CropMonitoring_Serializer(monitoring)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: Actualizar un monitoreo
    def put(self, request, pk):
        monitoring = self.get_object(pk)
        serializer = CropMonitoring_Serializer(monitoring, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Eliminar un monitoreo
    def delete(self, request, pk):
        monitoring = self.get_object(pk)
        monitoring.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
