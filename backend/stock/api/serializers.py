from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from stock.models import Articulo, Categoria, Deposito, Stock, Formula



class ArticuloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Articulo
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'categoria': instance.categoria.nombre,
            'codigo': instance.codigo,
            'precio_unitario': instance.precio_unitario,
            'punto_de_reorden': instance.punto_de_reorden,
            'vto': instance.vto,
            'lote': instance.lote
        }


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ('__all__')


class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields = ('id','articulo', 'deposito', 'cantidad', 'fecha_ingreso', 'cantidad_ingresada', 'fecha_salida', 'cantidad_salida')


class FormulaSerializer(serializers.ModelSerializer):
    articulo = ArticuloSerializer
    
    class Meta:
        model = Formula
        fields = ('__all__')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'producto': instance.producto.nombre,
            'articulo': instance.articulo.nombre,
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        fields = ('username', 'password')


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    token = serializers.CharField(source='key', read_only=True)

    class Meta:
        model = Token
        fields = ('user', 'token')
