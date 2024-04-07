from django.db import models

# Create your models here.

class Categoria(models.Model):
    '''
    Esta clase hereda de django models.Model, y crea una tabla llamada categorias,
    para almacenar las distintas categorias asignada a cada uno de los articulos.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=60, unique=True, verbose_name='Nombre de categoria')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Categoria, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    

class Articulo(models.Model):
    '''
    Genera una tabla que almacena articulos, y cada columna recibe el nombre de cada atributo
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=60, unique=True, verbose_name='Nombre articulo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=60)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lote = models.CharField(max_length=20, default=None, blank=True, null=True)
    vto = models.DateField(default=None, blank=True, null=True)
    punto_de_reorden = models.PositiveIntegerField(default=0) 
    # El punto de reorden es la cantidad minima de un artículo, a partir de la cual se debe
    # hacer una solicitud de reposicion.
    cantidad = models.PositiveIntegerField(default=0, blank=True, null=True)
     
    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Articulo, self).save(*args, **kwargs)
    
    def __str__(self):
        '''
        La función str representa lo que retorna cuando llamamos al objeto
        '''
        return self.nombre


class Formula(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    producto = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='producto', null=True, blank=True)

    def __str__(self):
        return str(self.producto)


class Deposito(models.Model):
    '''
    Genera una tabla que almacena los nombres de los distintos depositos.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=60, unique=True, verbose_name='Nombre Deposito')

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Deposito, self).save(*args, **kwargs)
    
    def __str__(self):
        '''
        La función str representa lo que retorna cuando llamamos al objeto
        '''
        return self.nombre


class Stock(models.Model):
    '''
    Genera una tabla que almacena las cantidades en stock de cada artículo de cada deposito.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    deposito = models.ForeignKey(Deposito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_ingreso = models.DateField(default=None, blank=True, null=True)
    cantidad_ingresada = models.PositiveIntegerField(default=0, blank=True, null=True)
    fecha_salida = models.DateField(default=None, blank=True, null=True)
    cantidad_salida = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.articulo)

