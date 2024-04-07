from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
from stock.models import Articulo, Categoria, Deposito, Stock, Formula


# Registro de los modelos en el admin
# class ArticuloResources(resources.ModelResource):
#     fields = (
#         'nombre',
#         'codigo',
#         'precio_unitario',
#         'punto_de_reorden',
#     )
#     class Meta:
#         model = Articulo

@admin.register(Articulo)
# class ArticuloAdmin(ImportExportModelAdmin):

#     resouce_class = ArticuloResources
class ArticuloAdmin(admin.ModelAdmin):
    
    fieldsets = (
       (None, {
           'fields': ('nombre', 'codigo', 'categoria', 'precio_unitario','cantidad')
       }),
       ('Advanced options', {
           'classes': ('collapse',),
           'fields': ('lote', 'vto', 'punto_de_reorden')
       })
    )
    list_display = ('id','nombre', 'codigo', 'categoria', 'precio_unitario', 'punto_de_reorden','cantidad')
    search_fields = ['nombre']
    list_filter = ('categoria',)
    list_display_links = ('nombre',)
    ordering = ['id']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    fields = ('id','nombre',)
    list_display = ('id','nombre',)


@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):
    fields = ('nombre',)


@admin.register(Stock)
class DepositoAdmin(admin.ModelAdmin):
    fields = ('articulo', 'deposito', 'cantidad','cantidad_ingresada','fecha_ingreso','cantidad_salida','fecha_salida')
    list_display = ('articulo', 'deposito', 'cantidad','cantidad_ingresada','fecha_ingreso','cantidad_salida','fecha_salida')
    list_filter = ('deposito',)
    search_fields = ['articulo']


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    fields = ('producto','articulo')
    list_display = ('producto','articulo')
    search_fields = ['producto']


# Modificación en título de panel de administración
admin.site.site_header = 'PlayTime - Sitio de Administración -'

# Modificación en leyenda de la pestaña de la hoja
admin.site.site_title = 'Playtime'
admin.site.index_title = 'Control de stock'
