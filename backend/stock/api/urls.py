from django.urls import path, include
from stock.api.viewsets import *
from stock.api.api_views import FormulaProductoList

urlpatterns = [
    path('api/', include('stock.api.routers')),
    path('formula/', FormulaProductoList.as_view())
]