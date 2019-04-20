#!/usr/bin/env python3

import jinja2
import sqlite3
from tabulate import tabulate


DB="base_de_datos.db"
CONEXION=sqlite3.connect(DB)

class GestorDB(object):
    def __init__(self, nombre_fichero_db):
        self.DB=nombre_fichero_db
        self.conexion=sqlite3.connect(self.DB)
        self.cursor=None
    def get_cursor(self, nuevo_cursor=False):
        if nuevo_cursor or self.cursor==None:
            self.cursor=self.conexion.cursor()
        return self.cursor
    
    def get_filas(self, sql, reiniciar_cursor=False):
        self.cursor=self.get_cursor(reiniciar_cursor)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        
        
    def get_filas_como_tabla_markdown(self, tabla):
        texto_tabla= tabulate(tabla, headers="firstrow", tablefmt="orgtbl")
        texto_tabla=texto_tabla.replace("+", "|")
        return texto_tabla
    
    def get_nombres_columnas_ultimo_sql(self):
        nombres_columnas = tuple([descripcion[0] for descripcion in self.cursor.description])
        return nombres_columnas
    
    def get_resultados_sql(self, sql, con_nombres_columnas=True):
        
        filas=self.get_filas(sql)
        lista_resultados=[]
        nombres_columnas = self.get_nombres_columnas_ultimo_sql()
        lista_resultados.append(nombres_columnas)
        
        tabla_resultados=lista_resultados+filas
        
        tabla_markdown=self.get_filas_como_tabla_markdown(tabla_resultados)
        return tabla_markdown
    
    def fila_aparece_en_tabla_resultados(self, fila, tabla_resultados):
        for f in tabla_resultados:
            if f==fila:
                return True
        #Fin del for
        return False
    
    def destacar_fila(self, fila):
        cadena_formato="**{0}**"
        fila_reformateada=[cadena_formato.format(columna) for columna in fila]
        return fila_reformateada
    
            
    def get_tabla_resaltada(self, sql1, sql2):
        """
        Devuelve una tabla con las filas de sql1 resaltados siempre y cuando dichas filas
        aparezcan en sql2
        """
        filas1=self.get_filas(sql1)
        filas_resultado=[self.get_nombres_columnas_ultimo_sql()]
        filas2=self.get_filas(sql2)
        
        
        for pos in range(0, len(filas1)):
            fila=filas1[pos]
            if self.fila_aparece_en_tabla_resultados(fila, filas2):
                filas_resultado.append(self.destacar_fila(fila))
            else:
                filas_resultado.append(fila)
        tabla_markdown=self.get_filas_como_tabla_markdown(filas_resultado)
        return tabla_markdown
    
    def get_resultados_sql_formateados(self, sql):
        texto="""
Consulta ``{0}``
    \n\n
    Resultado:\n\n
{1}
        """
        
        resultado_tabla=self.get_resultados_sql(sql)
        
        devolver=texto.format(sql, resultado_tabla)
        
        return devolver
            
        

def get_resultados_sql(sql):
    
    filas=get_filas(sql)
    lista_resultados=[]
    nombres_columnas = tuple([descripcion[0] for descripcion in cursor.description])
    lista_resultados.append(nombres_columnas)
    
    tabla=lista_resultados+filas
    texto_tabla= tabulate(tabla, headers="firstrow", tablefmt="orgtbl")
    texto_tabla=texto_tabla.replace("+", "|")
    return texto_tabla






    


def get_resultados_sql(sql):
    texto="""
Consulta ``{0}``
\n\n
Resultado:\n\n
{1}
    """
    
    resultado_tabla=gestor_db.get_resultados_sql(sql)
    
    devolver=texto.format(sql, resultado_tabla)
    
    return devolver
        
        
    
def generar_readme():
        
    DB="base_de_datos.db"
    gestor_db=GestorDB(DB)
    
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "Plantilla_README.md"
    
    template = templateEnv.get_template(TEMPLATE_FILE)
    diccionario=dict()
    
    
    diccionario["tabla_proveedores"]                =gestor_db.get_resultados_sql( "select * from proveedores")
    diccionario["tabla_partes"]                     =gestor_db.get_resultados_sql( "select * from partes")
    diccionario["tabla_proyectos"]                  =gestor_db.get_resultados_sql( "select * from proyectos")
    diccionario["tabla_suministra"]                 =gestor_db.get_resultados_sql( "select * from suministra")
    
    
    diccionario["ejemplo_from_01"]                  =gestor_db.get_resultados_sql("select * from productos, componentes")
    
    diccionario["select_nombre_proveedores"]        =gestor_db.get_resultados_sql( "select nombreprov from proveedores" )
    diccionario["select_nombre_ciudad_proveedores"] =gestor_db.get_resultados_sql ("select nombreprov, ciudad from proveedores")
    diccionario["tabla_partes_p1_destacado"]        =gestor_db.get_tabla_resaltada("select * from partes",
                                                                                   "select * from partes where color='Rojo'")
    diccionario["ejemplo_where_01"]                 =gestor_db.get_resultados_sql_formateados("select * from partes where color='Rojo'")
    
    resultado=template.render(diccionario)
    
    print(resultado)
    
if __name__ == '__main__':
    generar_readme()