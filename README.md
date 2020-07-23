CREATE DATABASE BDcuentas;
USE BDcuentas;

CREATE TABLE Grupo
(id INT PRIMARY KEY NOT null,
descripcion VARCHAR(20) NOT NULL unique);

CREATE TABLE plancuenta (
  id INT PRIMARY key AUTO_INCREMENT,
  codigo varchar(50) DEFAULT NULL,
  idgrupo int NOT NULL,
  descripcion varchar(50) not NULL,
  naturaleza varchar(1) not NULL,
  estado tinyint(1) NOT NULL,
 FOREIGN KEY (idgrupo) REFERENCES grupo (`id`));

create view if not exists view_plancuenta AS 
select pc.id Id, pc.codigo, pc.idgrupo as 'grupo', pc.descripcion, pc.naturaleza, pc.estado  
FROM plancuenta pc inner join grupo gp on pc.idgrupo = gp.id;
