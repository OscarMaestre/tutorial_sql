# Tutorial de SQL


## Requisitos



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
| y4            | Consola          | *Atenas* |
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
