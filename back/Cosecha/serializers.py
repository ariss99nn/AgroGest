from rest_framework import serializers
from .models import Harvest, Classification, Harvest_Type, Harvest_Details

class Classification_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'


class Harvest_Serializer(serializers.ModelSerializer):#creamos el serilizador de cosecha
    class Meta: #clase para mostrar los datos
        model = Harvest #seleccionamos el modelo de cosecha
        fields = '__all__' #los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)
        
class Harvest_type_Serializer(serializers.ModelSerializer):
    class Meta:#clase para mostrar los datos
        model = Harvest_Type#seleccionamos el modelo de tipo cosecha
        fields = '__all__'#los campos que se van a mostrar(ALL SE REIERE A TODOS LOS CAMPOS)
        
class HarvestDeatils_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Harvest_Details
        fields = '__all__'