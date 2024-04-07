import csv
from django.core.management.base import BaseCommand, CommandError
from stock.models import Categoria

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        categorias = []
        filename = input('Ingrese path del archivo.csv o el nombre con extensión.csv: ')
        # Abre el archivo csv utilizando with open
        try:
            with open(str(filename), 'r') as csvfile:
                # Lee los dtos y se almacenan en una lista de diccionarios
                
                    data = list(csv.reader(csvfile, delimiter=','))
                    
                    for row in data[1:]:
                        categorias.append(
                        Categoria(
                            nombre = row[0],
                            )
                        )
        except Exception as e:
             raise CommandError(e)
            
        if len(categorias) > 1:
            Categoria.objects.bulk_create(categorias)
        print('Se ha importado satistactoriamente las categorias')