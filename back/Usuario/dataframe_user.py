import pandas as pd
from Usuario.models import User  # Asegúrate de que esta ruta sea correcta

def dataframe_user():
    queryset = User.objects.all().values(
        'id', 'username', 'first_name', 'last_name',
        'document', 'phone', 'city', 'email',
        'role', 'is_active', 'last_login', 'created_at'
    )
    df = pd.DataFrame(list(queryset))
    
    # Opcional: renombrar columnas
    df.rename(columns={
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'document': 'Documento',
        'phone': 'Teléfono',
        'city': 'Ciudad',
        'email': 'Correo',
        'role': 'Rol',
        'is_active': 'Activo',
        'last_login': 'Último login',
        'created_at': 'Creado el',
    }, inplace=True)
    
    return df

