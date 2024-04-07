import csv
from django.core.management.base import BaseCommand, CommandError
from stock.models import Articulo,Categoria

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        articulos = []
        url = input('Ingrese path del archivo.css o el nombre con extensión.csv: ')
        # Abre el archivo csv utilizando with open
        try:
            with open(str(url), 'r') as csvfile:
                # Lee los dtos y se almacenan en una lista de diccionarios
                data = list(csv.reader(csvfile, delimiter=','))
                for row in data[1:]:
                    articulos.append(
                        Articulo(
                            codigo = row[0],
                            nombre = row[1],
                            categoria = Categoria.objects.get(nombre=row[2]),
                            precio_unitario = row[3],
                            lote = row[4],
                            vto = row[5],
                            punto_de_reorden = row[6],
                            cantidad = row[7],
                            )
                    )
        except:
            raise CommandError('No existe archivo.csv o el mismo es erróneo')
        
        if len(articulos) > 1:
            Articulo.objects.bulk_create(articulos)
        print('Se ha importado satistactoriamente los artículos')
