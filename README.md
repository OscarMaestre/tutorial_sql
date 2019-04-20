# Tutorial de SQL


## Pasos preliminares

Este tutorial usará ``sqlite3`` para hacer las consultas. Se adjunta el fichero ``base_de_datos.db`` que ya contiene todas las tablas y datos necesarios para hacer las consultas. También se adjunta el ejecutable de SQLite para Windows, en el archivo ``sqlite3.exe``. El fichero con la creación de tablas en forma de SQL puede encontrarse en el archivo ``base_de_datos.sql``.

En Linux se necesitará instalar ``sqlite3`` con el comando ``sudo apt-get install sqlite3`` y después ejecutar ``sqlite3 base_de_datos.db``

En Windows habrá que ir al símbolo del sistema, e ir al directorio donde se haya descargado (usando el comando ``cd <directorio>``) y despues ejecutar ``sqlite3 base_de_datos.db``.


## Tablas

A continuación se muestran las tablas que componen nuestra base de datos.La tabla proveedores es la siguiente


| numprov   | nombreprov   |   estado | ciudad   |
|-----------|--------------|----------|----------|
| v1        | Smith        |       20 | Londres  |
| v2        | Jones        |       10 | Paris    |
| v3        | Blake        |       30 | Paris    |
| v4        | Clarke       |       20 | Londres  |
| v5        | Adams        |       30 | Atenas   |


La tabla partes

| numparte   | nombreparte   | color   |   peso | ciudad   |
|------------|---------------|---------|--------|----------|
| p1         | Tuerca        | Rojo    |     12 | Londres  |
| p2         | Perno         | Verde   |     17 | Paris    |
| p3         | Tornillo      | Azul    |     17 | Roma     |
| p4         | Tornillo      | Rojo    |     14 | Londres  |
| p5         | Leva          | Azul    |     12 | Paris    |
| p6         | Engranaje     | Rojo    |     19 | Londres  |

La tabla proyectos

| numproyecto   | nombreproyecto   | ciudad   |
|---------------|------------------|----------|
| y1            | Clasificador     | Paris    |
| y2            | Monitor          | Roma     |
| y3            | OCR              | Atenas   |
| y4            | Consola          | Atenas   |
| y5            | RAID             | Londres  |
| y6            | EDS              | Oslo     |
| y7            | Cinta            | Londres  |

La tabla suministra

| numprov   | numparte   | numproyecto   |   cantidad |
|-----------|------------|---------------|------------|
| v1        | p1         | y1            |        200 |
| v1        | p1         | y4            |        700 |
| v2        | p3         | y1            |        400 |
| v2        | p3         | y2            |        200 |
| v2        | p3         | y3            |        300 |
| v2        | p3         | y4            |        500 |
| v2        | p3         | y5            |        600 |
| v2        | p3         | y6            |        400 |
| v2        | p3         | y7            |        600 |
| v2        | p5         | y2            |        100 |
| v3        | p3         | y1            |        200 |
| v3        | p4         | y2            |        500 |
| v4        | p6         | y3            |        300 |
| v4        | p6         | y7            |        300 |
| v5        | p2         | y2            |        200 |
| v5        | p2         | y4            |        100 |
| v5        | p5         | y5            |        500 |
| v5        | p6         | y2            |        200 |
| v5        | p1         | y4            |        100 |
| v5        | p3         | y4            |        200 |
| v5        | p4         | y4            |        800 |
| v5        | p5         | y4            |        400 |
| v5        | p6         | y4            |        500 |



# SQL

## Sintaxis básica

La sintaxis básica de una sentencia SQL es ``select <campo1>, <campo2>,...<campon> from <tabla1>, <tabla2>, <tabla3>``. Así, si deseamos solo mostrar el nombre de los proveedores podemos hacer esto:

| nombreprov   |
|--------------|
| Smith        |
| Jones        |
| Blake        |
| Clarke       |
| Adams        |

y si deseamos mostrar el nombre y la ciudad de los proveedores podemos hacer esto:

| nombreprov   | ciudad   |
|--------------|----------|
| Smith        | Londres  |
| Jones        | Paris    |
| Blake        | Paris    |
| Clarke       | Londres  |
| Adams        | Atenas   |


## WHERE

No siempre interesa recuperar todos los resultados de una tabla. Si por ejemplo deseamos que solo aparezcan aquellas filas que cumplan una cierta condición podemos usar WHERE.


Supongamos que queremos ver qué partes son rojas. Si examinamos la tabla partes veremos esto (obsérvese que hemos destacado las filas con los resultados que se supone que deben salir):

| numparte   | nombreparte   | color   | peso   | ciudad    |
|------------|---------------|---------|--------|-----------|
| *p1*       | *Tuerca*      | *Rojo*  | *12*   | *Londres* |
| p2         | Perno         | Verde   | 17     | Paris     |
| p3         | Tornillo      | Azul    | 17     | Roma      |
| *p4*       | *Tornillo*    | *Rojo*  | *14*   | *Londres* |
| p5         | Leva          | Azul    | 12     | Paris     |
| *p6*       | *Engranaje*   | *Rojo*  | *19*   | *Londres* |

Así que nuestra consulta con WHERE será así:



Consulta ``select * from partes where color='Rojo'``
    


    Resultado:


| numparte   | nombreparte   | color   |   peso | ciudad   |
|------------|---------------|---------|--------|----------|
| p1         | Tuerca        | Rojo    |     12 | Londres  |
| p4         | Tornillo      | Rojo    |     14 | Londres  |
| p6         | Engranaje     | Rojo    |     19 | Londres  |
        
