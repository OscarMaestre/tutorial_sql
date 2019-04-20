DB=base_de_datos.sql

all: reconstruir_db
	./rellenar_plantilla.py > index.html; mv index.html docs

reconstruir_db:
	rm $(DB); cat tablas_y_valores.sql | sqlite3 $(DB)