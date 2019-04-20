CREATE TABLE productos (
    id_producto integer primary key,
    nombre_producto varchar(40)
);

CREATE TABLE componentes (
    id_componente integer,
    id_producto   integer,
    nombre_componente varchar(40),
    primary key (id_componente, id_producto)
);
CREATE TABLE proveedores (
	numprov varchar(3) primary key, 		
	nombreprov varchar(8), 
	estado tinyint, 
	ciudad varchar(15)
);

CREATE TABLE partes (
   numparte varchar(3) primary key,
   nombreparte varchar(9), 
   color varchar(6), 
   peso tinyint, 
   ciudad varchar(8)
);

CREATE TABLE proyectos (
   numproyecto varchar(3) primary key,
   nombreproyecto varchar(13),
   ciudad varchar(8)
);

CREATE TABLE suministra (
  numprov varchar(3)
      references proveedores(numprov), 
  numparte varchar(3)
      references partes(numparte), 
  numproyecto varchar(3)
      references proyectos(numproyecto),
  cantidad int,
  primary key (numprov,numparte, numproyecto)
);

INSERT INTO proveedores VALUES('v1','Smith',20,'Londres');
INSERT INTO proveedores VALUES('v2','Jones',10,'Paris');
INSERT INTO proveedores VALUES('v3','Blake',30,'Paris');
INSERT INTO proveedores VALUES('v4','Clarke',20,'Londres');
INSERT INTO proveedores VALUES('v5','Adams',30,'Atenas');

INSERT INTO partes VALUES('p1','Tuerca','Rojo',12,'Londres');
INSERT INTO partes VALUES('p2','Perno','Verde',17,'Paris');
INSERT INTO partes VALUES('p3','Tornillo','Azul',17,'Roma');
INSERT INTO partes VALUES('p4','Tornillo','Rojo',14,'Londres');
INSERT INTO partes VALUES('p5','Leva','Azul',12,'Paris');
INSERT INTO partes VALUES('p6','Engranaje','Rojo',19,'Londres');


INSERT INTO proyectos VALUES('y1','Clasificador','Paris');
INSERT INTO proyectos VALUES('y2','Monitor','Roma');
INSERT INTO proyectos VALUES('y3','OCR','Atenas');
INSERT INTO proyectos VALUES('y4','Consola','Atenas');
INSERT INTO proyectos VALUES('y5','RAID','Londres');
INSERT INTO proyectos VALUES('y6','EDS','Oslo');
INSERT INTO proyectos VALUES('y7','Cinta','Londres');



INSERT INTO suministra VALUES('v1','p1','y1',200);
INSERT INTO suministra VALUES('v1','p1','y4',700);
INSERT INTO suministra VALUES('v2','p3','y1',400);
INSERT INTO suministra VALUES('v2','p3','y2',200);
INSERT INTO suministra VALUES('v2','p3','y3',300);
INSERT INTO suministra VALUES('v2','p3','y4',500);
INSERT INTO suministra VALUES('v2','p3','y5',600);
INSERT INTO suministra VALUES('v2','p3','y6',400);
INSERT INTO suministra VALUES('v2','p3','y7',600);
INSERT INTO suministra VALUES('v2','p5','y2',100);
INSERT INTO suministra VALUES('v3','p3','y1',200);
INSERT INTO suministra VALUES('v3','p4','y2',500);
INSERT INTO suministra VALUES('v4','p6','y3',300);
INSERT INTO suministra VALUES('v4','p6','y7',300);
INSERT INTO suministra VALUES('v5','p2','y2',200);
INSERT INTO suministra VALUES('v5','p2','y4',100);
INSERT INTO suministra VALUES('v5','p5','y5',500);
INSERT INTO suministra VALUES('v5','p6','y2',200);
INSERT INTO suministra VALUES('v5','p1','y4',100);
INSERT INTO suministra VALUES('v5','p3','y4',200);
INSERT INTO suministra VALUES('v5','p4','y4',800);
INSERT INTO suministra VALUES('v5','p5','y4',400);
INSERT INTO suministra VALUES('v5','p6','y4',500);

INSERT INTO productos VALUES(1,'Monitor');
INSERT INTO productos VALUES(2,'Teclado');
INSERT INTO productos VALUES(3,'Altavoz');


INSERT INTO componentes VALUES(1,1,'Tornillo');
INSERT INTO componentes VALUES(1,2,'Tornillo');
INSERT INTO componentes VALUES(2,3,'Transistor');
