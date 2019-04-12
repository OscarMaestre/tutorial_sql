#!/usr/bin/env python3

import jinja2
import sqlite3
from tabulate import tabulate


DB="base_de_datos.db"
CONEXION=sqlite3.connect(DB)


def get_tabla_formateada(sql):
    conexion=CONEXION
    cursor=conexion.cursor()
    cursor.execute(sql)
    lista_resultados=[]
    nombres_columnas = tuple([descripcion[0] for descripcion in cursor.description])
    lista_resultados.append(nombres_columnas)
    filas=cursor.fetchall()
    tabla=lista_resultados+filas
    texto_tabla= tabulate(tabla, headers="firstrow", tablefmt="orgtbl")
    texto_tabla=texto_tabla.replace("+", "|")
    return texto_tabla
        
        
    
    
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "Plantilla_README.md"

template = templateEnv.get_template(TEMPLATE_FILE)
diccionario=dict()


diccionario["tabla_proveedores"]    =get_tabla_formateada( "select * from proveedores")
diccionario["tabla_partes"]         =get_tabla_formateada( "select * from partes")
diccionario["tabla_proyectos"]      =get_tabla_formateada( "select * from proyectos")
diccionario["tabla_suministra"]     =get_tabla_formateada( "select * from suministra")


diccionario["ejemplo_from_01"]      =get_tabla_formateada("select * from productos, componentes")

diccionario["select_nombre_proveedores"]=get_tabla_formateada( "select nombreprov from proveedores" )
diccionario["select_nombre_ciudad_proveedores"]=get_tabla_formateada ("select nombreprov, ciudad from proveedores")
resultado=template.render(diccionario)

print(resultado)