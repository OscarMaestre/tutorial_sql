DB=base_de_datos.sql

all: reconstruir_db
	./crear_readme.py > README.md

reconstruir_db:
	rm $(DB); cat tablas_y_valores.sql | sqlite3 $(DB)