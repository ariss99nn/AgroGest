from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .dataframe_user import dataframe_user
import pandas as pd

class ExportUserExcelView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        df = dataframe_user()

        # Convertir cualquier columna datetime con timezone a tz-naive
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                try:
                    df[col] = df[col].dt.tz_localize(None)
                except (AttributeError, TypeError):
                    pass  # No es un datetime con zona horaria

        # Preparar respuesta con tipo de contenido Excel
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=usuarios.xlsx'

        # Guardar el DataFrame en la respuesta
        df.to_excel(response, index=False)
        return response