# Property Micro Service
Property Micro Service: es herramienta en la que sus usuarios puedan consultar los inmuebles
disponibles para la venta. En esta herramienta los usuarios deben ser capaces de ver tanto los
inmuebles vendidos como los disponibles. Con el objetivo de hacer más fácil la búsqueda, se
espera que los usuarios puedan aplicar diferentes filtros a la búsqueda.

Tecnologías
----------------------------
[x] Linux - Ambiente de desarrollo.
[x] IDE Visual Studio Code
[x] Git - Versionar código.
[x] PyPI - Instalar y administrar paquetes.
[x] Virtualenv - Instalar librerías solo para el entorno virtual del proyecto.
[x] API Rest.
[x] JSON - Para intercambio de datos.
[x] WSGI - Servidor Web.
[x] SQLAlchemy - Conexión a la base de datos.
[x] MYSQL - Librería para conexión a la base de datos.

Lenguajes
----------------------------
[x] Suporte para Python 3.8 o mayor
[x] SQL para consultas

Servicio de “Me gusta”
----------------------------
1. El diagra de Entidad-Relación se encuentra en el proyecto dentro de la ruta src/doc/sql.
2. El codifo SQL de las tablas se encuentra en el proyecto dentro de la ruta src/doc/sql.

Instalación de dependencias
----------------------------
```
  sudo apt update
  apt-get install build-essential python-dev
  $ pip install -r requirements.txt
```

Dudas
----------------------------
1.- ¿Conexión a la base de datos, que librería usar? 

El candidato es usar pyodbc ya que he trabajado por mucho tiempo con esta librería  
porque tiene soporte para crear SQL nativo, ejecutar procesos almacenados, funciones  
sin embargo, tiene algunas dependencias al momento de descargar de Pipy falla la instalación;  
la solución es actualizar los paquetes a nivel sistema operativo dependiendo del sistema operativo,  
pero otra parte es que no he probado con conexión a la base de datos en MySQL.  
Y la última opción es ocupar la librería SQLAlchemy, en este caso no he tenido mucha experiencia 
con conexión a MySQL y con SQL nativo ya que he trabajado más con ORM, la ventaja de que hay mucha documentación
y soporte a base de datos relacionales. 


2.- Proponer un mejor modelo de la estructura actual de base de datos: 

En el diagrama Entidad Relación no se maneja histórico de la propiedad, aquí mi duda es más con el requerimiento del cliente y la historia de usuario de lo que se espera en él manejo del histórico de la propiedad y de cómo se va dando la etapa de cada propiedad como: comprando, comprado, pre_venta, en_venta y por último vendido entonces si se debe manejar un histórico. 
 
En mi propuesta no la maneje porque dentro de la tabla de property abrir una llave foránea con el catálogo de status_id, con la intención de manejar el ultimo status que se encuentra la propiedad y cada vez que vaya en el proceso de compra de una propiedad se vaya actualizando el registro en el campo 'status_id' y junto con la fecha de modificación. Esto también con la finalidad de que la consulta sea más rápida y facilitar el acceso de un registro de propiedad en el estado que se encuentra. 

En el diagrama ER la tabla extendida es la de rating el cual está relacionado con la tabla de usuarios, 
y la tabla de property. Cuando un usuario le dé me gusta una propiedad se quede registrado en la tabla de rating en el campo "score" se puede manejar con un 0=No me gusta ó 1=Me gusta, en el caso de que se quiera manejar con la votación por puntaje de 5 estrellas lo soportaría sin problemas por eso no lo deje como un campo booleano. 

Igual cuenta con un campo "message" para escribir un mensaje a la propiedad como recomendación. Además, tiene un campo fecha de creación del registro en "created". 

