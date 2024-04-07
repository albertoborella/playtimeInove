# Proyecto de Playtime

El fin de este proyecto es armar un sistema de control de stock y gestión de inventario. Para ello se utilizan las siguientes tecnologías:
- Frontend con React JS
- Backend con Django
- IA utilizando visión por computadora y machine learning

### Sobre el cliente
Playtime es una empresa que arma juegos de plaza para todos los parques en Argentina, una empresa que manipula una gran cantidad de insumos y materia prima para transformar tornillos, tubos y fierros en juegos aptos para niños.

### Objetivo
Lo que se busca es un sistema de control de stock y gestión de inventario que posea las siguientes características:
- Posibilidad de administrar desde un panel de control el stock/inventario de diversas piezas (de ahora en más llamada artículos).
- Utilizar el celular y su cámara trasera para realizar la lectura de códigos QR o códigos de barra que permitan encuestar en el sistema el stock de dicho artículo.
- Posibilidad de, una vez encontrar el item en el sistema, agregar o desconectar stock.
- Poder administrar perfiles de usuarios (administrador, supervisor, usario común) para determinar quienes tienen acceso a ver el stock y quienes tiene acceso a modificarlo, como así también quien tiene acceso al panel de control general.
- La página que se utilice para la lectura y captura del código debe ser simple, a fin de facilitar el uso a un operario que en simultaño puede estar realizando otras tareas que requieran de su atención.


Playtime acutalmente utiliza Tango, pero no posee una manera rápida y cómoda desde un celular de poder leer un código QR o código de barra para conocer rapidamente el stock de un artículo.

### Valor agregado
- Permitir exportar/importar inventario en CSV, a fin de sincronizar información con otros sistemas como Tango y evitar carga manual.
- Crear algoritmos de recomendación de cantidad de ingreso de stock basado en análisis de datos para acelerar la carga manual de inventario.
- Alertas configurables de artículo próximo a quedar sin stock


### Modelo de negocio (modelo de datos)
- Un artículo representa a cualquier pieza, desde la más chica a la más grande, la cual puede pertenecer a una cierta categoría.
- Un artículo a su vez puede tener asociado una "formula". Una fórmula indica que otros artículos se necesitan para armar ese artículo.
- Formula es una entidad que lleva dos foreign_key de la misma tabla (articulo), es por eso que debe utilizanrse related_name para que Django los pueda diferenciar (investigar más en la documentación de Django.)
- El stock será asociado a un cierto artículo y a un cierto depósito.
- punto_de_reorden es la cantidad mínima de stock del artículo en la cual se considera peligroso y se debe solicitar su reposición. Este valor comienza por defecto en 0 (es decir, cuando no hay más stock se lanza la alarma de reposición).
-

Ver esquema de modelo de datos propuesto:
[Diagrama de entidades](playtime_db.drawio.pdf)


### Épicas por rol
Backend:
- Setup de la aplicación e implementación del modelo de datos
- Implementar y customizar el django admin
- APIs para consumo de imágenes QR o código de barras
- APIs para importar/exportar datos
- APIs para los dashboard

Frontend:
- Setup frontend y organización del proyecto y las vistas
- Pantalla Login/Logout
- Pantalla para lectura de código QR o código de barras y/o librería para análisis de la imagen
- Pantalla con el stock disponible (consulta)
- Pantalla para agregar stock
- Librería para gráfico de datos en el frontend

IA:
- Generar datos para la prueba y ensayo del sistema (mocks)
- Algoritmos de visión por computadora para lectura de código QR y código de barras (primero analizar si puede realizarse en el frontend)
- Algoritmo de predicción de cantidad de stock a agregar
- Algoritmo de análisis de stock (predicción de consumo, clusterización/agrupación, detección de piezas críticas
- Algoritmos para nutrir de información los dashboard
- Librería para gráfico de datos en el frontend

