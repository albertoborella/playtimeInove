from django.http import HttpResponse
import csv
from .models import Articulo, Categoria


def export_articulos_csv(request):
    '''
    Esta función exporta los artiulos desde la base de datos a un archivo formato .csv
    '''
    queryset = Articulo.objects.all()
    # Obtengo los campos del modelo
    options = Articulo._meta
    fields = [field.name for field in options.fields]
    # Genero la respuesta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'atachment; filename="articulos.csv"'
    writer = csv.writer(response)
    # Escribo la cabecera
    writer.writerow([options.get_field(field).verbose_name for field in fields])
    # Escribo los datos
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    return response


def import_articulos_csv(request):
        '''
        Esta función importa los artículos desde un archivo en formato .csv
        '''
        categorias = Categoria.objects.all()
        if categorias:
             
            articulos = []
            with open('articulos.csv', 'r') as csv_file:
                data = list(csv.reader(csv_file, delimiter=','))
                for row in data[1:]:
                    articulos.append(
                        Articulo(
                            codigo = row[0],
                            nombre = row[1].upper(),
                            categoria = Categoria.objects.get(nombre=row[2]),
                            precio_unitario = row[3],
                            lote = row[4],
                            vto = row[5],
                            punto_de_reorden = row[6],
                            cantidad = row[7],
                                )
                            )
                if len (articulos) > 0:
                    Articulo.objects.bulk_create(articulos)

                return HttpResponse('Base de datos Articulo, importada con éxito!!')
        else:
             return HttpResponse('Debes primero incorporar categorias en tabla Categoria')
             


def export_categorias_csv(request):
    '''
    Esta función exporta las categorias desde la base de datos a un archivo formato .csv
    '''
    queryset = Categoria.objects.all()
    # Obtengo los campos del modelo
    options = Categoria._meta
    fields = [field.name for field in options.fields]
    # Genero la respuesta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'atachment; filename="categorias.csv"'
    writer = csv.writer(response)
    # Escribo la cabecera
    writer.writerow([options.get_field(field).verbose_name for field in fields])
    # Escribo los datos
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    return response


def import_categorias_csv(request):
        '''
        Esta función importa las categorias desde un archivo en formato .csv
        '''
        categorias = []
        with open('categorias.csv', 'r') as csv_file:
            data = list(csv.reader(csv_file, delimiter=','))
            for row in data[1:]:
                categorias.append(
                    Categoria(
                        nombre=row[0].upper()
                  )
            )
        if len (categorias) > 0:
            Categoria.objects.bulk_create(categorias)

        return HttpResponse('Base de datos Categoria, importada con éxito!!')
        

