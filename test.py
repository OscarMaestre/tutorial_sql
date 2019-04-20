#!/usr/bin/env python3

import unittest
import crear_readme



class Test(unittest.TestCase):
    
    def test_fila_dentro_de_tabla(self):
        DB="base_de_datos.db"
        gestor_db=crear_readme.GestorDB(DB)
        sql1="select * from partes"
        sql2="select * from partes where numparte='p1'"
        filas1=gestor_db.get_filas(sql1)
        filas2=gestor_db.get_filas(sql2)
        print(filas1)
        print(filas2)
        
        esta_presente=gestor_db.fila_aparece_en_tabla_resultados(filas2[0], filas1)
        self.assertEqual(esta_presente, True)
        
        fila_reformateada=gestor_db.destacar_fila(filas2[0])
        print(fila_reformateada)
        
        tabla=gestor_db.get_tabla_resaltada(sql1, sql2)
        print(tabla)
        
    
    
if __name__ == '__main__':
    unittest.main()