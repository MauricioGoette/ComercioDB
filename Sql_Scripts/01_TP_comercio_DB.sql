
-------------Bases de Datos - Trabajo Integrador - ComercioDB-----------
--	Mauricio Goette
--	Creacion base de datos
--  Creacion de tablas


-------------------------Tablas---------------------------------------------

--1--Cliente: (PK)cuit_cliente, nombre_cliente, apellido_cliente, razon_social, direccion, telefono
--2--Proveedor: (PK)cuit_proveedor, nombre_proveedor, telefono_proveedor, direccion_proveedor, mail_proveedor, cbu_proveedor, dolar_proveedor
--3--Producto: (PK)id_producto, (FK)cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, precio_venta, meses_garantia
--4--Venta: (PK)id_venta, (FK)cuit_cliente, fecha_venta
--5--Venta_Detalle: (PK,FK)id_venta, (PK,FK)id_producto, cantidad_producto, total venta
--6--Servicio: (PK)id_servicio, (PK)descripcion_servicio, (FK)cuit_cliente, fecha_servicio, contrasenia_usuario, cantidad_servicio, total_servicio
--7--Compra: (PK)id_compra, (FK)cuit_proveedor, fecha_compra
--8--Compra_Detalle: (PK,FK)id_compra, (PK,FK)id_producto, cantidad_compra, precio_unitario, total_producto
--9--Inventario: (PK,FK)id_producto, stock_producto

------------------------------Crear_Base_Datos-------------------------------

CREATE DATABASE comerciodb
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       --PASSWORD = "elgranKathogas3"
       TEMPLATE template0
       TABLESPACE = pg_default
       --LC_COLLATE = 'es_ES.UTF-8'
       --LC_CTYPE = 'es_ES.UTF-8'
       CONNECTION LIMIT = -1;
      
--CREATE USER morris WITH ENCRYPTED PASSWORD 'elgranKathogas3';
--GRANT ALL PRIVILEGES ON DATABASE comerciodb TO morris;     
     
      
-- Para borrar la base de datos comerciodb
-- DROP DATABASE comerciodb;

---Establecer comerciodb como objeto activo----

-------------------------------Crear_Tablas---------------------------------------------

--1--Cliente: (PK)cuit_cliente, nombre_cliente, apellido_cliente, razon_social, direccion, telefono

CREATE TABLE cliente
(
id_cliente serial not null, 
cuit_cliente character varying(11),
nombre_cliente character varying(75),
apellido_cliente character varying(75),
razon_social character varying(75),
direccion character varying(100),
telefono character varying(75),
CONSTRAINT pk_cliente PRIMARY KEY (id_cliente)
);
COMMENT ON TABLE cliente
  IS 'Tabla donde se almacenar?n los clientes del comercio.';
 
 
 -------------------------------------------------------------------------
 
--2--Proveedor: (PK)cuit_proveedor, nombre_proveedor, telefono_proveedor, direccion_proveedor, mail_proveedor, cbu_proveedor, dolar_proveedor

CREATE TABLE proveedor
(
cuit_proveedor character varying(11),
nombre_proveedor character varying(75),
telefono_proveedor character varying(75),
direccion_proveedor character varying(100),
mail_proveedor character varying(100),
cbu_proveedor character varying(75),
dolar_proveedor numeric(10,3),
CONSTRAINT pk_proveedor PRIMARY KEY (cuit_proveedor)
);
COMMENT ON TABLE proveedor
  IS 'Tabla donde se almacenar?n los proveedores del comercio.';
 
-----------------------------------------------------------------------------

--3--Producto: (PK)id_producto, (FK)cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, precio_venta, meses_garantia

CREATE TABLE producto
(
id_producto serial not null,
cuit_proveedor character varying(11),
nombre_producto character varying(100),
descripcion_producto character varying(150),
marca character varying(75),
modelo character varying(75),
categoria character varying(75),
codigo character varying(75),
precio_compra numeric(10,3),
precio_venta1 numeric(10,3),
precio_venta2 numeric(10,3),
precio_venta3 numeric(10,3),
meses_garantia integer,
CONSTRAINT pk_producto PRIMARY KEY (id_producto),
CONSTRAINT fk_producto_cuit_proveedor FOREIGN KEY (cuit_proveedor)
      REFERENCES proveedor (cuit_proveedor) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO action
);
COMMENT ON TABLE producto
  IS 'Tabla donde se almacenar?n los productos';
 

---------------------------------------------------------------------------------

--4--Venta: (PK)id_venta, (FK)cuit_cliente, fecha_venta

CREATE TABLE venta
(
id_venta serial not null,
id_cliente integer,
fecha_venta date not null default now(), 
CONSTRAINT pk_venta PRIMARY KEY (id_venta),
CONSTRAINT fk_venta_id_cliente FOREIGN KEY (id_cliente)
      REFERENCES cliente (id_cliente) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);
COMMENT ON TABLE venta
  IS 'Tabla donde se almacenar?n las ventas del comercio.';
 
--------------------------------------------------------------------------------
 
 --5--Venta_Detalle: (PK,FK)id_venta, (PK,FK)id_producto, cantidad_producto, total_venta
 
 CREATE TABLE venta_detalle
(
id_venta serial not null,
id_producto integer,
cantidad_producto integer,
total_venta numeric(10,3), 
CONSTRAINT pk_venta_detalle PRIMARY KEY (id_venta, id_producto),
CONSTRAINT fk_venta_id_venta FOREIGN KEY (id_venta)
      REFERENCES venta (id_venta) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_venta_id_producto FOREIGN KEY (id_producto)
      REFERENCES producto (id_producto) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);
COMMENT ON TABLE venta_detalle
  IS 'Tabla donde se almacenar? el detalle la venta del comercio.';
 
---------------------------------------------------------------------------------

--6--Servicio: (PK)id_servicio, (PK)descripcion_servicio, (FK)cuit_cliente, fecha_servicio, contrasenia_usuario, cantidad_servicio, total_servicio

CREATE TABLE servicio
(
id_servicio serial not null,
id_cliente integer,
fecha_servicio date not null default now(),
descripcion_servicio character varying(150) not null,
contrasenia_usuario character varying(75) default 'No Password',
cantidad_servicio integer,
total_servicio numeric(10,3),
CONSTRAINT pk_servicio PRIMARY KEY (id_servicio, descripcion_servicio),
CONSTRAINT fk_servicio_id_cliente FOREIGN KEY (id_cliente)
      REFERENCES cliente (id_cliente) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO action
);
COMMENT ON TABLE servicio
  IS 'Tabla donde se almacenar?n los servicios';

------------------------------------------------------------------------------------

--7--Compra: (PK)id_compra, (FK)cuit_proveedor, fecha_compra

CREATE TABLE compra
(
id_compra serial not null,
cuit_proveedor character varying(11),
fecha_compra date not null default now(),
CONSTRAINT pk_compra PRIMARY KEY (id_compra),
CONSTRAINT fk_compra_cuit_proveedor FOREIGN KEY (cuit_proveedor)
      REFERENCES proveedor (cuit_proveedor) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);
COMMENT ON TABLE compra
  IS 'Tabla donde se almacenar?n las compras del comercio.';
 
-------------------------------------------------------------------------------

--8--Compra_Detalle: (PK,FK)id_compra, (PK,FK)id_producto, cantidad_compra, precio_unitario

CREATE TABLE compra_detalle
(
id_compra serial not null,
id_producto integer,
cantidad_compra integer,
precio_unitario numeric(10,3),
CONSTRAINT pk_compra_detalle PRIMARY KEY (id_compra, id_producto),
CONSTRAINT fk_compra_id_compra FOREIGN KEY (id_compra)
      REFERENCES compra (id_compra) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_compra_id_producto FOREIGN KEY (id_producto)
      REFERENCES producto (id_producto) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);
COMMENT ON TABLE compra_detalle
  IS 'Tabla donde se almacenar?n el detalle de las compras del comercio.';
 
-------------------------------------------------------------------------------

--9--Inventario: (PK,FK)id_producto, stock_producto

CREATE TABLE inventario
(
id_producto integer,
stock_producto integer,
CONSTRAINT pk_inventario PRIMARY KEY (id_producto),
CONSTRAINT fk_inventario_id_producto FOREIGN KEY (id_producto)
      REFERENCES producto (id_producto) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO action
);
COMMENT ON TABLE inventario
  IS 'Tabla donde se almacenar?n la cantidad de productos del inventario';
 
 

 