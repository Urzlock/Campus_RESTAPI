from rest_framework import serializers
from CampusService.models import Campus

#FORMA 1 DE HACERLO
class CampusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required = False, max_length=250)
    calle = serializers.CharField(required = False, max_length=250)
    numexterior = serializers.CharField(required = False, max_length=250)
    ciudad = serializers.CharField(required = False, max_length=250)
    estado = serializers.CharField(required = False, max_length=250)
    codigopostal = serializers.CharField(required = False, max_length=250)
    telcontacto = serializers.CharField(required = False, max_length=250)

    def create(self, validated_data):
         return Campus.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.calle = validated_data.get('calle', instance.calle)
        instance.numexterior = validated_data.get('numexterior', instance.numexterior)
        instance.ciudad = validated_data.get('ciudad', instance.ciudad)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.codigopostal = validated_data.get('codigopostal', instance.codigopostal)
        instance.telcontacto = validated_data.get('telcontacto', instance.telcontacto)
        instance.save()
        return instance
    
 
    #FORMA 2
# class CampusSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Campus
#             fields =['id','nombre','calle','colonia','numexterior','ciudad','estado','codigopostal','telcontacto']