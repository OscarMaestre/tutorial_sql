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
    
    
    def get_celdas_fila(self, fila, marca_html="td", con_destacado=False):
        celda="<{1}>{0}</{1}>"
        if con_destacado:
            celda="<{1} class='celdadestacada'>{0}</{1}>"
        lista_celdas=[celda.format(campo, marca_html) for campo in fila]
        celdas_html="".join(lista_celdas)
        celdas_html="<tr>"+celdas_html+"</tr>"
        return celdas_html
    
    def get_filas_como_tabla_html(self, filas):
        total_filas=len(filas)
        tabla="<table class='table'><thead>{0}</thead><tbody>{1}</tbody></table>"
        celdas_cabecera=self.get_celdas_fila(filas[0], marca_html="th")
        
        celdas_datos=""
        for pos in range(1, total_filas):
            celdas_datos+=self.get_celdas_fila(filas[pos])
        tabla_final=tabla.format(celdas_cabecera, celdas_datos)
        return tabla_final
        
    def get_nombres_columnas_ultimo_sql(self):
        nombres_columnas = tuple([descripcion[0] for descripcion in self.cursor.description])
        return nombres_columnas
    
    def get_resultados_sql(self, sql, con_nombres_columnas=True):
        
        filas=self.get_filas(sql)
        lista_resultados=[]
        nombres_columnas = self.get_nombres_columnas_ultimo_sql()
        lista_resultados.append(nombres_columnas)
        
        tabla_resultados=lista_resultados+filas
        
        tabla_markdown=self.get_filas_como_tabla_html(tabla_resultados)
        return tabla_markdown
    
    def fila_aparece_en_tabla_resultados(self, fila, tabla_resultados):
        for f in tabla_resultados:
            if f==fila:
                return True
        #Fin del for
        return False
    
    def destacar_fila(self, fila):
        cadena_formato="*{0}*"
        fila_reformateada=[cadena_formato.format(columna) for columna in fila]
        return fila_reformateada
    
    def destacar_fila_html(self, fila):
        cadena_formato="<span class='celdadestacada'>{0}</span>"
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
                filas_resultado.append(self.destacar_fila_html(fila))
            else:
                filas_resultado.append(fila)
        tabla_markdown=self.get_filas_como_tabla_html(filas_resultado)
        return tabla_markdown
    
    def get_resultados_sql_formateados(self, sql):
        texto="""
<div class="resultadoconsulta">
    <div class="textosql">{0}</div>
    <div class="resultadosql">Resultado:<br/>{1}</div>
</div>
        """
        
        resultado_tabla=self.get_resultados_sql(sql)
        
        devolver=texto.format(sql, resultado_tabla)
        
        return devolver
            
        
        
        
    
def generar_readme():
        
    DB="base_de_datos.db"
    gestor_db=GestorDB(DB)
    
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "Plantilla_index.html"
    
    template = templateEnv.get_template(TEMPLATE_FILE)
    diccionario=dict()
    
    
    diccionario["tabla_proveedores"]                =gestor_db.get_resultados_sql( "select * from proveedores")
    diccionario["tabla_partes"]                     =gestor_db.get_resultados_sql( "select * from partes")
    diccionario["tabla_proyectos"]                  =gestor_db.get_resultados_sql( "select * from proyectos")
    diccionario["tabla_suministra"]                 =gestor_db.get_resultados_sql( "select * from suministra")
    
    
    diccionario["ejemplo_from_01"]                  =gestor_db.get_resultados_sql("select * from productos, componentes")
    
    diccionario["select_nombre_proveedores"]        =gestor_db.get_resultados_sql_formateados( "select nombreprov from proveedores" )
    diccionario["select_nombre_ciudad_proveedores"] =gestor_db.get_resultados_sql_formateados ("select nombreprov, ciudad from proveedores")
    diccionario["tabla_partes_p1_destacado"]        =gestor_db.get_tabla_resaltada("select * from partes",
                                                                                   "select * from partes where color='Rojo'")
    diccionario["ejemplo_where_01"]                 =gestor_db.get_resultados_sql_formateados("select * from partes where color='Rojo'")
    
    diccionario["select_cod_prov_ciudad"]           =gestor_db.get_resultados_sql_formateados("select numprov, ciudad from proveedores")
    diccionario["select_cod_proyecto_ciudad"]       =gestor_db.get_resultados_sql_formateados("select numproyecto, ciudad from proyectos")
    
    diccionario["select_proveedores_proyectos_misma_ciudad_sin_where"]=gestor_db.get_resultados_sql_formateados(
        "select numprov, proveedores.ciudad, numproyecto, proyectos.ciudad from proveedores, proyectos")
    
    diccionario["select_proveedores_proyectos_misma_ciudad_con_where"]=gestor_db.get_resultados_sql_formateados(
        "select numprov, proveedores.ciudad, numproyecto, proyectos.ciudad from proveedores, proyectos "+
        "where proveedores.ciudad=proyectos.ciudad")
    
    
    diccionario["select_proveedores_proyectos_misma_ciudad_con_where"]=gestor_db.get_resultados_sql_formateados(
        "select numprov, proveedores.ciudad, numproyecto, proyectos.ciudad from proveedores, proyectos "+
        "where proveedores.ciudad=proyectos.ciudad")
    
    diccionario["ejemplo_inner_join_01"]=gestor_db.get_resultados_sql_formateados(
        "select numprov, proveedores.ciudad, numproyecto, proyectos.ciudad from proveedores inner join proyectos"+
        " on proveedores.ciudad=proyectos.ciudad;")
    

    resultado=template.render(diccionario)
    
    print(resultado)
    
if __name__ == '__main__':
    generar_readme()