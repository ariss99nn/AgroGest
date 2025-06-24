from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import User_Serializer
from .permissions import IsAdminOrOwner

class UserListCreateAPIView(APIView):
    """
    Lista todos los usuarios o crea uno nuevo.
    Solo disponible para usuarios con rol ADMIN.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'ADMIN':
            return Response({"detail": "No autorizado."}, status=status.HTTP_403_FORBIDDEN)
        users = User.objects.all()
        serializer = User_Serializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != 'ADMIN':
            return Response({"detail": "No autorizado."}, status=status.HTTP_403_FORBIDDEN)
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateDestroyAPIView(APIView):
    """
    Permite a un ADMIN consultar/editar/eliminar cualquier usuario.
    Permite a un AGRICULTOR consultar/editar solo su propio perfil.
    """
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = User_Serializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        serializer = User_Serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class UserMeAPIView(APIView):
    """
    Vista para que el usuario autenticado pueda consultar y editar su propio perfil.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retorna los datos del usuario actual
        serializer = User_Serializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        # Actualiza los datos del usuario actual (de forma parcial)
        serializer = User_Serializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)