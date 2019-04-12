# Tutorial de SQL


## Pasos preliminares

Este tutorial usará ``sqlite3`` para hacer las consultas. Se adjunta el fichero ``base_de_datos.db`` que ya contiene todas las tablas y datos necesarios para hacer las consultas. También se adjunta el ejecutable de SQLite para Windows, en el archivo ``sqlite3.exe``. El fichero con la creación de tablas en forma de SQL puede encontrarse en el archivo ``base_de_datos.sql``.

En Linux se necesitará instalar ``sqlite3`` con el comando ``sudo apt-get install sqlite3`` y después ejecutar ``sqlite3 base_de_datos.db``

En Windows habrá que ir al símbolo del sistema, e ir al directorio donde se haya descargado (usando el comando ``cd <directorio>``) y despues ejecutar ``sqlite3 base_de_datos.db``.


## Tablas

A continuación se muestran las tablas que componen nuestra base de datos.La tabla proveedores es la siguiente


{{tabla_proveedores}}


La tabla partes

{{tabla_partes}}

La tabla proyectos

{{tabla_proyectos}}

La tabla suministra

{{tabla_suministra}}



# SQL

## Sintaxis básica

La sintaxis básica de una sentencia SQL es ``select <campo1>, <campo2>,...<campon> from <tabla1>, <tabla2>, <tabla3>``. Así, si deseamos solo mostrar el nombre de los proveedores podemos hacer esto:

{{select_nombre_proveedores}}

y si deseamos mostrar el nombre y la ciudad de los proveedores podemos hacer esto:

{{select_nombre_ciudad_proveedores}}