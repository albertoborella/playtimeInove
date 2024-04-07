from rest_framework import viewsets
from .serializers import (ArticuloSerializer, CategoriaSerializer, DepositoSerializer,
                           StockSerializer, FormulaSerializer)


# Viewsets
 
class ArticuloViewSet(viewsets.ModelViewSet):
    serializer_class = ArticuloSerializer
    queryset = serializer_class.Meta.model.objects.all()
    

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = serializer_class.Meta.model.objects.all()


class DepositoViewSet(viewsets.ModelViewSet):
    serializer_class = DepositoSerializer
    queryset = serializer_class.Meta.model.objects.all()


class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = serializer_class.Meta.model.objects.all()


class FormulaViewSet(viewsets.ModelViewSet):
    serializer_class = FormulaSerializer
    queryset = serializer_class.Meta.model.objects.all()