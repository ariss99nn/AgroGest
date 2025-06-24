from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Prediction
from .serializers import predictionSerializer


class PredictionListCreateAPIView(APIView):
    def get(self, request):
        predictions = Prediction.objects.all()
        serializer = predictionSerializer(predictions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = predictionSerializer(data=request.data)
        # Guardar con campo 'created_by' si hay usuario autenticado
        if serializer.is_valid():
            serializer.save(created_by=request.user if request.user.is_authenticated else None)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictionRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Prediction.objects.get(pk=pk)
        except Prediction.DoesNotExist:
            raise Http404("Prediction not found")

    def get(self, request, pk):
        prediction = self.get_object(pk)
        serializer = predictionSerializer(prediction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        prediction = self.get_object(pk)
        serializer = predictionSerializer(prediction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prediction = self.get_object(pk)
        prediction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
