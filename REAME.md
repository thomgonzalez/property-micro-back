¿Conexión a la base de datos, que libreria usar ?

El candidato es usar pyodbc ya que he trabajado por mucho tiempo con esta librería 
porque tiene soporte para crear SQL nativo, ejecutar procesos almacenados, funciones  
sin embargo, tiene algunas dependencias al momento de descargar de Pipy y falla en la instalación; 
la solución es actualizar los paquetes a nivel sistema operativo dependiendo del sistema operativo,  
pero otra parte es que no he probado con conexión a la base de datos en MySQL. 

Y la última opción es ocupar la librería SQLAlchemy, en este caso no he tenido mucha experiencia 
con conexión a MySQL y con SQL nativo ya que he trabajado más con ORM, la ventaja de que hay mucha documentación 
y soporte a base de datos relacionales. 