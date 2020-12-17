drop database alumnos_db;

create database alumnos_db;

use alumnos_db;

CREATE TABLE usuario (
  id int(5) NOT NULL primary key auto_increment,
  codigo varchar(50) NOT NULL,
  nombre varchar(50) NOT NULL,
  email varchar(50) NOT NULL,
  contra varchar(50) NOT NULL,
  tipo varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into usuario(codigo,nombre,email,contra,tipo)
values ('999888777','Jaime','jaime@abc.com','asdqwe','profesor');
