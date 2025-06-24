from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Input
from .serializers import Input_Serializer
# Create your views here.

class Input_List_View(APIView):
    # GET: Lista todos los registros de Input
    def get(self, request):
        inputs = Input.objects.all()  # Trae todos los objetos Input de la base de datos
        serializer = Input_Serializer(inputs, many=True)  # Serializa la lista
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Crea un nuevo registro de Input
    def post(self, request):
        serializer = Input_Serializer(data=request.data)
        if serializer.is_valid():  # CORREGIDO: Se añadió ()
            serializer.save()  # Guarda si es válido
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Input_Detail_View(APIView):
    # Método auxiliar para obtener un objeto o lanzar 404
    def get_object(self, pk):
        try:
            return Input.objects.get(pk=pk)
        except Input.DoesNotExist:
            raise Http404("Input not found")

    # GET: Obtiene los datos de un solo Input
    def get(self, request, pk):
        input_instance = self.get_object(pk)
        serializer = Input_Serializer(input_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: Actualiza un Input existente
    def put(self, request, pk):
        input_instance = self.get_object(pk)
        serializer = Input_Serializer(input_instance, data=request.data)
        if serializer.is_valid():  # CORREGIDO: Se añadió ()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Elimina un Input por su ID
    def delete(self, request, pk):
        input_instance = self.get_object(pk)
        input_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        