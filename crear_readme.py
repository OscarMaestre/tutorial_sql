#!/usr/bin/env python3

import jinja2
import sqlite3
from tabulate import tabulate


DB="base_de_datos.db"
CONEXION=sqlite3.connect(DB)


def get_tabla_formateada(conexion, sql):
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


diccionario["tabla_proveedores"]=get_tabla_formateada(CONEXION, "select * from proveedores")
diccionario["tabla_partes"]=get_tabla_formateada(CONEXION, "select * from partes")
diccionario["tabla_proyectos"]=get_tabla_formateada(CONEXION, "select * from proyectos")
diccionario["tabla_suministra"]=get_tabla_formateada(CONEXION, "select * from suministra")

resultado=template.render(diccionario)

print(resultado)