from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Investment
from .serializers import Investment_Serializer

#CLASE PARA LISTAR Y CREAR INVERSIONES
class Investment_List_View(APIView):
    # GET: Lista todas las inversiones
    def get(self, request):
        investments = Investment.objects.all()
        serializer = Investment_Serializer(investments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Crea una nueva inversión
    def post(self, request):
        serializer = Investment_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#CLASE PARA DETALLAR Y ACTUALIZAR INVERSIONES
class Investment_Detail_View(APIView):
    # Método auxiliar para obtener un objeto o lanzar 404
    def get_object(self, pk):
        try:
            return Investment.objects.get(pk=pk)
        except Investment.DoesNotExist:
            raise Http404("Investment not found")

    # GET: Obtener detalle de una inversión
    def get(self, request, pk):
        investment = self.get_object(pk)
        serializer = Investment_Serializer(investment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: Actualizar una inversión
    def put(self, request, pk):
        investment = self.get_object(pk)
        serializer = Investment_Serializer(investment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Eliminar una inversión
    def delete(self, request, pk):
        investment = self.get_object(pk)
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
