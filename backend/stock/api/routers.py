from .viewsets import ArticuloViewSet, CategoriaViewSet, DepositoViewSet, StockViewSet, FormulaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'articulos', ArticuloViewSet, basename='articulos')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'depositos', DepositoViewSet, basename='depositos')
router.register(r'stocks', StockViewSet, basename='stocks')
router.register(r'formulas', FormulaViewSet, basename='formulas')

urlpatterns = router.urls