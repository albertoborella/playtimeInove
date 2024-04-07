# Playtime - Backend

## Instalacion
El presente proyecto está realizado en Python3, y se deberá tener instalado el mismo para correr el proyecto

## Backend del proyecto
Para correr el backend del proyecto se puede optar por alguna de las siguientes metodologías:
1.- A traves del sistema Docker
2.- A través de la creación de un entorno virtual con todas las dependencias.

## 1.- DOCKER
1.- Primero se deberá crear el contenedor en cada una de las computadoras (con docker instalado), a traves del comando:
**$** `docker-compose buil backend` (backend es el nombre del contenedor en el actual proyecto)

2.- Una vez creado el contenedor, y posicionado en la carpeta dentro de la cual está el Dockerfile y el
docker-compose, correr el proyecto a traves del siguiente comando:
**$** `docker-compose up`

3.- Para detener la ejecucion del contenedor y del servidor se pueden utilizar los siguientes comandos:
`ctrl + c` o `docker-compose down`

4.- Tener en cuenta que segun la configuracion de permisos que cada uno tenga en su maquina, es posible que antes
de la colocacion de cada comando tengan que agregar sudo y luego la password de cada uno


## 2.- Entorno Virtual 
Con el objetivo de tener juntas, todas las dependencias que se vayan utilizando en el proyecto se crea un entorno virtual donde se van a alojar todas las dependencias que se vayan necesitando. Para instalar el entorno utilizar estando posicionados en el proyecto colocar el siguiente comando:

python3 -m venv <nombre del entorno> 

### Activar el Entorno Virtual
Una vez creado en entorno, para trabajar en el mismo, se debe activar utilizando los siguientes comandos una vez posicionados en la carpeta donde fue creado el entorno:

En linux:    source <nombre del entorno>/bin/activate
En windows:  <nombre del entorno>\Scripts\activate.bat


### Instalar las librerias en el entorno creado
Una vez creado y activado el entorno virtual (fijarce que si está activado, al incio del prompt se debe ver entre paréntesis en nombre del entorno), se deben descargar todas las dependencias que estan el archivo requirements.txt del backend. Para esto se aplica el siguiente comando:

pip install -r requirements.txt

### Lanzar el proyecto

Una vez posicionado en la carpeta donde está el proyecto, aplicar el sigiente comando:
python manage.py runserver, y el proyecto correrá en el puerto 8000
http://127.0.0.1:8000

## Swagger/Redoc

Se ha instalado y configurado Swagger y Redoc, a fin de que se puedan ver y analizar los endpoints de API
Una vez ingresado en la aplicación, llendo a http://127.0.0.1:8000/swagger o http://127.0.0.1:8000/redoc se
podra visualizar cada uno de los endpoint, y llendo a http://127.0.0.1:8000/admin se ingresa en el administrador de Django (usuario: admin password: admin)

## Tabla Formula

En esta tabla el administrador puede formar Productos, que a la vez se encuentran en la tabla Articulo y que a la vez 
estén conformados por mas de un artículo que también se encuentran en la tabla Articulo.
A titulo de ejemplo pueden ver lo que regresa el siguiente endpoint:
`http://127.0.0.1:8000/stock/formula/?producto=62`

## Validaciones

En las tablas Categoria, Articulo y Depósito, se han validado en que los nombres de categorias, productos o depósitos
no pueden existir nombres duplicados, sino que deben ser únicos.
También, si bien no es una validación propiamente dicha, en esos modelos los datos de los nombres ingresados, se pueden ingresar tanto en mayúsculas como minúsculas, pero siempre serán transformados en mayúsculas

