from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Permite acceso a:
    - Usuarios con rol ADMIN (acceso completo).
    - Usuarios AGRICULTOR solo a su propio objeto.
    - Para métodos seguros (GET, HEAD, OPTIONS) o para PUT.
    - Bloquea DELETE u otros métodos que no quieras para agricultores.
    """

    def has_permission(self, request, view):
        # Solo usuarios autenticados pueden continuar
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin tiene acceso total
        if request.user.role == 'ADMIN':
            return True
        
        # Agricultor puede acceder solo a su propio objeto
        if request.user.role == 'AGRICULTOR' and obj == request.user:
            # Permitir GET, HEAD, OPTIONS y PUT
            if request.method in permissions.SAFE_METHODS or request.method == 'PUT':
                return True
            
            # Bloquear DELETE u otros métodos
            return False
        
        return False
