DB=base_de_datos.sql

all: reconstruir_db
	./crear_readme.py > README.md ; markdown README.md > tutorial.html

reconstruir_db:
	rm $(DB); cat tablas_y_valores.sql | sqlite3 $(DB)