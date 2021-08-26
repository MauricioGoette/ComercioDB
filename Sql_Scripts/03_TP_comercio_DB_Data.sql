
-------------Bases de Datos - Trabajo Integrador - ComercioDB-----------
--	Mauricio Goette
--	Ingreso de datos a las tablas


----------------------------Tablas Finales---------------------------------------------

--1--Cliente: (PK)cuit_cliente, nombre_cliente, apellido_cliente, razon_social, direccion, telefono, id_cliente
--2--Proveedor: (PK)cuit_proveedor, nombre_proveedor, telefono_proveedor, direccion_proveedor, mail_proveedor, cbu_proveedor, dolar_proveedor, proveedor_id, proveedor_status
--3--Producto: (PK)id_producto(s), (FK)cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, precio_venta, meses_garantia
--4--Venta: (PK)id_venta, (FK)cuit_cliente, fecha_venta
--5--Venta_Detalle: (PK,FK)id_venta, (PK,FK)id_producto, cantidad_producto
--6--Servicio: (PK)id_servicio, (PK)descripcion_servicio, (FK)cuit_cliente, fecha_servicio, contrasenia_usuario, cantidad_servicio, total_servicio
--7--Compra: (PK)id_compra, (FK)cuit_proveedor, fecha_compra
--8--Compra_Detalle: (PK,FK)id_compra, (PK,FK)id_producto, cantidad_compra, precio_unitario
--9--Inventario: (PK,FK)id_producto, stock_producto
-------------------------------------------------------------------------------------------------------------------------------------

--1--Cliente: (PK)cuit_cliente, nombre_cliente, apellido_cliente, razon_social, direccion, telefono
insert into cliente (cuit_cliente, nombre_cliente, apellido_cliente, razon_social, direccion, telefono) values
('27378557653', 'Geraldine', 'Cepeda', 'Consumidor Final', 'Las Heras 160 - Crespo', '03435011532'),
('20363029060', 'Ignacio', 'Meier', 'Monotributista', 'Alberdi 1615 - Crespo', '03434158766'),
('27456878951', 'Jorge', 'Schneider', 'Responsable inscripo', 'Los sauces - Ramirez', '03434896587'),
('20333135273','Mauricio','Goette','Monotributista','25 de Mayo 619 - Crespo','03434477864');

--2--Proveedor: (PK)cuit_proveedor, nombre_proveedor, telefono_proveedor, direccion_proveedor, mail_proveedor, cbu_proveedor, dolar_proveedor
insert into proveedor (cuit_proveedor, nombre_proveedor, telefono_proveedor, direccion_proveedor, mail_proveedor, cbu_proveedor, dolar_proveedor) values
('20465789373','Datatech','03454568794', 'San Martin 487 - Santa Fe', 'datatech@hotmail.com','54879787465465454189561',81.5),
('30651655516', 'Elit SA', '03424550015', 'San Luis 2659 - Santa Fe', 'elitweb@elit.com.ar', '0070079520000006921846', 85),
('30709274712', 'Mobe SRL', '03434625754', 'Almirante Brown 1812 - Santa Fe', 'info@mobesel.com.ar', '2850365130000061719418', 86.5),
('30711603499', 'Alport SRL', '03435097450', 'Alsina 829 - Parana', 'm.dachary@intrahard.com', '0720192520000000986140', 85),
('27240717226', 'Arroba PC', '03436219358','Almafuerte 257 - Parana', 'arrobapc@gmail.com', '2850365140017061727463', 85);
				
--3--Producto: (PK)id_producto, (FK)cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, precio_venta, meses_garantia
insert into producto (cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, precio_venta, meses_garantia) values 
('20465789373', 'Kingston 32gb', 'Pendrive 32gb usb 3.0 Negro', 'Kingston','Kpd32', 'Pen drive','pdk32', 3.23, 5.24, 6),
('30651655516', 'AMD Ryzen 7 3700x', 'Procesador Ryzen 7 3700x AMD Matisse - Cooler Wraith spire', 'AMD', 'Ryzen 7 3700X', 'Microprocesador AM4', 'mpamd73700', 418, 550, 12),
('30709274712', 'Logitech G Pro Hero Gaming', 'Mouse cableado - Logitech G Pro Hero Gaming - 26000 DPI', 'Logitech', 'G Pro Hero Gaming', 'Mouse cableado', 'mlgphg', 37.84, 45, 12),
('30711603499', 'Asus X570-Plus', 'Placa Madre Asus x570-plus TUPF Gaming', 'Asus', 'X570-Plus', 'Motherboard Socket AM4', 'pmax570', 350, 420, 12),
('30651655516', 'Kingston A400 120 GB', 'Disco Solido SSD 120 GB', 'Kingston', 'A400', 'Disco Solido SSD Sata', 'dsk120', 25, 35, 6),
('30651655516', 'Kingston A400 240 GB', 'Disco Solido SSD 240 GB', 'Kingston', 'A400', 'Disco Solido SSD Sata', 'dsk240', 35, 45, 6),
('27240717226', 'Brother HL-1200', 'Impresora Laser Monocromatica', 'Brother', 'HL-1200', 'Impresora Monocromatica', 'ilbhl1200', 150, 200, 12);


		
--4--Venta: (PK)id_venta, (FK)cuit_cliente, fecha_venta
insert into venta (cuit_cliente, fecha_venta) values 
('27378557653', '2020-11-15'),
('20333135273', current_date),
('20363029060', current_date);
	
		
--5--Venta_Detalle: (PK,FK)id_venta, (PK,FK)id_producto, cantidad_producto
insert into venta_detalle (id_venta, id_producto, cantidad_producto) values
(3, 3, 1),
(1, 1, 2),
(2, 2, 1);


--6--Servicio: (PK)id_servicio, (PK)descripcion_servicio, (FK)cuit_cliente, fecha_servicio, contrasenia_usuario, cantidad_servicio, total_servicio
insert into servicio (cuit_cliente, fecha_servicio, descripcion_servicio, contrasenia_usuario, cantidad_servicio, total_servicio) values 
('27378557653', current_date, 'Reparacion Sistema windows 10', 'gera2020', 1, 1200),
('20333135273', '2020-11-10', 'Instalacion office 2016', default, 1, 600);
			
--7--Compra: (PK)id_compra, (FK)cuit_proveedor, fecha_compra
insert into compra (cuit_proveedor, fecha_compra) values
('30651655516', current_date),
('30709274712', current_date);

			
--8--Compra_Detalle: (PK,FK)id_compra, (PK,FK)id_producto, cantidad_compra, precio_unitario
insert into compra_detalle (id_compra, id_producto, cantidad_compra, precio_unitario) values
(1, 2, 1, 418),
(2, 3, 2, 75.68);
			
--9--Inventario: (PK,FK)id_producto, stock_producto
insert into inventario (id_producto, stock_producto) values
(1, 1),
(3, 2);
