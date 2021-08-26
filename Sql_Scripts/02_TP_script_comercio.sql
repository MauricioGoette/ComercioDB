-------------Bases de Datos - Trabajo Integrador - ComercioDB-----------
--	Mauricio Goette
--	DDL - DML
--	Creacion de procedimientos Procedimientos - Funciones 


--------------------------------------Clientes------------------------------------------------------

--Utilizadas via cursor en python
--select * from cliente
--select * from cliente order by {Opcion}

----------------------------------------------------------------------------------------------------

-- Agregar cliente
CREATE or replace procedure agregar_cliente (pcuit_cliente varchar, pnombre_cliente varchar, papellido varchar, prazon_social varchar, pdireccion varchar, ptelefono varchar)
LANGUAGE sql
AS $procedure$
	insert into cliente (cuit_cliente, nombre_cliente, apellido_cliente, razon_social, direccion, telefono) 
	select pcuit_cliente, pnombre_cliente, papellido, prazon_social, pdireccion, ptelefono;
$procedure$;

--drop procedure agregar_cliente
--call agregar_cliente ('20123456789', 'Jose', 'Gomez', 'Consumidor Final', 'San Martin 123 - Crespo', '0343151234678');


-- Editar cliente
alter table cliente 
add id_cliente serial;

--Actualizar datos cliente
CREATE or replace PROCEDURE actualizar_cliente(pid_cliente integer, pcuit_cliente varchar, pnombre_cliente varchar, papellido_cliente varchar, prazon_social varchar, pdireccion varchar, ptelefono varchar)
LANGUAGE sql 
AS $procedure$
	UPDATE cliente 
		SET cuit_cliente = pcuit_cliente, nombre_cliente = pnombre_cliente, apellido_cliente = papellido_cliente, razon_social = prazon_social, direccion = pdireccion, telefono = ptelefono
		where id_cliente = pid_cliente
$procedure$;

--drop procedure actualizar_cliente
--call actualizar_cliente (8, '20123456789', 'Jose', 'Ramirez', 'Consumidor Final', 'San Martin 123 - Crespo', '0343151234567');

--Buscar cliente por nombre
create or replace function public.buscar_cliente_nombre(nombre_buscar varchar)
returns table (cuit varchar, nombre varchar, apellido varchar, rsocial varchar, direccion varchar, telefono varchar, id int )
language sql
as $function$
	select c.cuit_cliente, c.nombre_cliente, c.apellido_cliente, c.razon_social, c.direccion, c.telefono, c.id_cliente 
	from cliente c
	where lower(c.nombre_cliente) like concat('%', lower(nombre_buscar), '%')
	order by c.nombre_cliente
$function$;

--drop function buscar_cliente_nombre
--select * from buscar_cliente_nombre ('Jo');

--Buscar cliente por apellido
create or replace function public.buscar_cliente_apellido(apellido_buscar varchar)
returns table (cuit varchar, nombre varchar, apellido varchar, rsocial varchar, direccion varchar, telefono varchar, id int )
language sql
as $function$
	select c.cuit_cliente, c.nombre_cliente, c.apellido_cliente, c.razon_social, c.direccion, c.telefono, c.id_cliente 
	from cliente c
	where lower(c.apellido_cliente) like concat('%', lower(apellido_buscar), '%')
	order by c.apellido_cliente, c.nombre_cliente 
$function$;

--drop function buscar_cliente_apellido
--select * from buscar_cliente_apellido ('ra');


------------------------------------Proveedores----------------------------------------------------
--Utilizadas via cursor en python

--select * from proveedor order by proveedor_id
--update proveedor set dolar_proveedor = {Dolar} where cuit_proveedor = '{cuit}'
--update proveedor set proveedor_status = '{estado}' where cuit_proveedor = '{cuit}'

----------------------------------------------------------------------------------------------------

--Agregar Id a la tabla proveedor
alter table proveedor 
add proveedor_id serial;

--Agregar status a proveedor (Activo - Inactivo)
alter table proveedor 
add proveedor_status char(1) default 'A';

--Agregar proveedor
CREATE or replace procedure agregar_proveedor (pcuit_proveedor varchar, pnombre_proveedor varchar, ptelefono varchar, pdireccion varchar, pmail varchar, pcbu varchar, pdolar numeric )
LANGUAGE sql
AS $procedure$
	insert into proveedor (cuit_proveedor, nombre_proveedor, telefono_proveedor, direccion_proveedor, mail_proveedor, cbu_proveedor, dolar_proveedor) 
	select pcuit_proveedor, pnombre_proveedor, ptelefono, pdireccion, pmail, pcbu, pdolar;
$procedure$;

--drop procedure agregar_proveedor
--call agregar_proveedor ('20987654321', 'Electroshop', '0343157654321', 'Sarmiento 789 - Ramirez', 'secretaria@electroshop.com', '01234567899876543210', 86);


---------------------------------------------Productos------------------------------------------------------
--Utilizadas via cursor en python

------Mostrar Productos Con el precio en pesos----
--select distinct p.id_producto, p.descripcion_producto, p.codigo, p.precio_venta, multiplicar(p.precio_venta, p2.dolar_proveedor), p2.nombre_proveedor from producto p, proveedor p2
--where p.cuit_proveedor = p2.cuit_proveedor
--order by p.id_producto 

------- Mostrar stock-----------
--select p.id_producto, p.nombre_producto, i.stock_producto from producto p
--join inventario i on i.id_producto = p.id_producto 

-----------------------------------------------------------------------------------------------------------

--Agregar ganancia al precio del producto en toda la tabla (Sin restriccion)
update producto set precio_venta1 = (precio_compra * 20 / 100) + precio_compra;
update producto set precio_venta2 = (precio_compra * 33 / 100) + precio_compra;
update producto set precio_venta3 = (precio_compra * 50 / 100) + precio_compra;

--update proveedor set dolar_proveedor numeric(10,3),

--Funcion para multiplicar 
create function multiplicar (x numeric, y numeric)
returns numeric
language sql
as $$
	select x * y;
$$;

--drop function multiplicar

--Buscar producto
create or replace function public.buscar_producto(nombre varchar)
returns table (id int, nombre varchar, descripcion varchar, categoria varchar, codigo varchar, precio_venta1 numeric, precio_venta2 numeric, precio_venta3 numeric)
language sql
as $function$
	select p.id_producto, p.nombre_producto, p.descripcion_producto, p.categoria, p.codigo, multiplicar(p.precio_venta1, p2.dolar_proveedor) as precio_venta1, multiplicar(p.precio_venta2, p2.dolar_proveedor) as precio_venta2, multiplicar(p.precio_venta3, p2.dolar_proveedor) as precio_venta3 
	from producto p, proveedor p2
	where lower(p.descripcion_producto) like concat('%', lower(nombre), '%') and
	p.cuit_proveedor = p2.cuit_proveedor
	order by p.id_producto 
$function$;

--drop function buscar_producto
--select * from buscar_producto ('Amd');
 

--Agregar producto
CREATE or replace procedure agregar_producto (pcuit_proveedor varchar, pnombre_producto varchar, pdescripcion_producto varchar, pmarca varchar, pmodelo varchar, pcategoria varchar, pcodigo varchar, pprecio_compra numeric, pmeses_garantia int)
LANGUAGE sql
AS $procedure$
	insert into producto (cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, meses_garantia) 
	select pcuit_proveedor, pnombre_producto, pdescripcion_producto, pmarca, pmodelo, pcategoria, pcodigo, pprecio_compra, pmeses_garantia;
	update producto set precio_venta1 = (precio_compra * 20 / 100) + precio_compra;
	update producto set precio_venta2 = (precio_compra * 33 / 100) + precio_compra;
	update producto set precio_venta3 = (precio_compra * 50 / 100) + precio_compra;
$procedure$;

--drop procedure agregar_prodcuto
--call agregar_producto('30711603499', 'Thermaltake Ryzen v200', 'Gabinete Negro con fuente 500W', 'Thermaltake', 'V200', 'Gabinete', 'gabrv200', 155, 200, 12);


-------------------------------------------Ventas-------------------------------------------------------

--Dar de baja la columna total venta, ya que se visualizara su resultado en la vista orden_venta
ALTER TABLE venta_detalle DROP COLUMN total_venta cascade;


-- Crear vista con los datos de la venta
create view orden_venta as
select v.id_venta, v.fecha_venta, c.nombre_cliente , c.apellido_cliente, c.razon_social, p.nombre_producto, multiplicar(p.precio_venta1, p2.dolar_proveedor) as precio_pesos1, multiplicar(p.precio_venta2, p2.dolar_proveedor) as precio_pesos2, multiplicar(p.precio_venta3, p2.dolar_proveedor) as precio_pesos3, vd.cantidad_producto, 
multiplicar (vd.cantidad_producto, p.precio_venta1) * p2.dolar_proveedor as total_venta1, multiplicar (vd.cantidad_producto, p.precio_venta2) * p2.dolar_proveedor as total_venta2, multiplicar (vd.cantidad_producto, p.precio_venta3) * p2.dolar_proveedor as total_venta3   
from cliente c, producto p, venta v, venta_detalle vd, proveedor p2 
where v.id_cliente = c.id_cliente
	and v.id_venta = vd.id_venta 
	and vd.id_producto = p.id_producto
	and p2.cuit_proveedor = p.cuit_proveedor
order by v.id_venta desc;

--drop view orden_venta
--select * from orden_venta;


--Agregar venta
create or replace procedure agregar_venta (pcuit_cliente varchar, pfecha_venta date, pid_producto int, pcantidad int)
LANGUAGE plpgsql 
AS $procedure$
declare 
	last_id integer;
begin
	insert into venta (cuit_cliente, fecha_venta) 
		values (pcuit_cliente, pfecha_venta)
		returning id_venta into last_id;
	insert into venta_detalle (id_venta, id_producto, cantidad_producto) 
		values (last_id, pid_producto, pcantidad);
	if exists (select i.id_producto from inventario i where pid_producto = i.id_producto) then
		update inventario i
		set stock_producto = stock_producto - pcantidad
		where pid_producto = i.id_producto;
	end if;
end;
$procedure$;	

--drop procedure agregar_venta
--call agregar_venta ('20123456789', '2020-11-23', 2, 3);


--Realizar venta de mas productos en la ultima venta
create or replace procedure misma_venta (pid_producto int, pcantidad int)
LANGUAGE plpgsql 
AS $procedure$
declare 
	last_id integer = max(id_venta) from venta ;
begin
	insert into venta_detalle (id_venta, id_producto, cantidad_producto) 
		values (last_id , pid_producto, pcantidad);
	if exists (select i.id_producto from inventario i where pid_producto = i.id_producto) then
		update inventario i
		set stock_producto = stock_producto - pcantidad
		where pid_producto = i.id_producto;
	end if;
end;
$procedure$;

--drop procedure misma_venta
--call misma_venta (3, 8);

--Opcional return id
--insert into venta (cuit_cliente, fecha_venta) values ('20333135273', '2020-11-19') returning id_venta; --Nos sql standar


------------------------------------------Servicios--------------------------------------------------
--Utilizadas via cursor en python
--select * from servicio s 

-----------------------------------------------------------------------------------------------------

--Crear vista ver servicios
create view orden_servicio as
select s.id_servicio, s.fecha_servicio, c.nombre_cliente , c.apellido_cliente, s.contrasenia_usuario, s.descripcion_servicio, s.cantidad_servicio, s.total_servicio 
from cliente c, servicio s
where s.id_cliente = c.id_cliente
order by s.id_servicio desc;

--drop view orden_servicio
--select * from orden_servicio;

-- Agregar servicio
CREATE or replace procedure agregar_servicio (pcuit_cliente varchar, pfecha_servicio date, pdescripcion varchar, pcontrasenia varchar, pcantidad int, ptotal_servicio numeric)
LANGUAGE plpgsql 
AS $procedure$
begin 
	if pcontrasenia = '' then
		insert into servicio (cuit_cliente, fecha_servicio, descripcion_servicio, cantidad_servicio, total_servicio) 
		select pcuit_cliente, pfecha_servicio, pdescripcion, pcantidad, ptotal_servicio;
	else
		insert into servicio (cuit_cliente, fecha_servicio, descripcion_servicio, contrasenia_usuario, cantidad_servicio, total_servicio) 
		select pcuit_cliente, pfecha_servicio, pdescripcion, pcontrasenia, pcantidad, ptotal_servicio;
	end if;
end;
$procedure$;

--drop procedure agregar_servicio
--call agregar_servicio ('20333135273', '2020-11-20', 'Win nuevo','', 1, 800.00);
--call agregar_servicio ('20333135273', '2020-11-22', 'Win 10', 'jojo', 1, 800.00);

--Agregar al mismo servicio
create or replace procedure mismo_servicio (pdescripcion varchar, pcantidad_servicio int, ptotal_servicio numeric)
LANGUAGE plpgsql 
AS $procedure$
declare 
	last_id integer = max(id_servicio) from servicio;
	last_cuit varchar = distinct cuit_cliente FROM servicio  WHERE id_servicio = (SELECT MAX(id_servicio) FROM servicio);
begin
	insert into servicio (id_servicio, cuit_cliente, descripcion_servicio, cantidad_servicio, total_servicio) 
	values (last_id, last_cuit, pdescripcion, pcantidad_servicio, ptotal_servicio);
end;
$procedure$;

--drop procedure mismo_servicio
--call mismo_servicio ('Reparacion videos4 ', 1, 900);


------------------------------------------------------------Compras ------------------------------------------------------------

--Crear vista compras
create view ver_compras_detalle as
select c.id_compra, p.nombre_proveedor, c.fecha_compra, p2.nombre_producto, cd.cantidad_compra, cd.precio_unitario, multiplicar (cd.cantidad_compra, cd.precio_unitario) as total_dolar from compra c
join compra_detalle cd on cd.id_compra = c.id_compra 
join proveedor p on p.cuit_proveedor = c.cuit_proveedor 
join producto p2 on p2.id_producto = cd.id_producto 
order by c.id_compra desc;

--drop view ver_compras_detalle
--select * from ver_compras_detalle;


--Agregar compra
CREATE or replace procedure agregar_compra (pcuit_proveedor varchar, pfecha_compra date, pid_producto int, pcantidad_compra int, pprecio_unitario numeric)
LANGUAGE plpgsql 
AS $procedure$
declare last_id int;
begin
	insert into compra (cuit_proveedor, fecha_compra)
		values (pcuit_proveedor, pfecha_compra)
		returning id_compra into last_id;
	insert into compra_detalle (id_compra, id_producto, cantidad_compra, precio_unitario)
		values (last_id, pid_producto, pcantidad_compra, pprecio_unitario);	
	if exists (select i.id_producto from inventario i where pid_producto = i.id_producto) then
		update inventario i
		set stock_producto = stock_producto + pcantidad_compra
		where pid_producto = i.id_producto;		
	else
		insert into inventario (id_producto, stock_producto)
		values (pid_producto, pcantidad_compra);
	end if;
end;
$procedure$;

--drop procedure agregar_compra
--call agregar_compra ('20987654321', '2020-11-23', 5, 5, 250);
 

--Agregar productos en la ultima compra
create or replace procedure misma_compra (pid_producto int, pcantidad_compra int, pprecio_unitario numeric)
LANGUAGE plpgsql 
AS $procedure$
declare 
	last_id integer = max(id_compra) from compra ;
begin
	insert into compra_detalle (id_compra, id_producto, cantidad_compra, precio_unitario)
		values (last_id, pid_producto, pcantidad_compra, pprecio_unitario);	
	if exists (select i.id_producto from inventario i where pid_producto = i.id_producto) then
		update inventario i
		set stock_producto = stock_producto + pcantidad_compra
		where pid_producto = i.id_producto;		
	else
		insert into inventario (id_producto, stock_producto)
		values (pid_producto, pcantidad_compra);
	end if;
end;
$procedure$;

--drop procedure misma_compra
--call misma_compra (4, 3, 99);

-------------------------------------------------------------------------------------------------------------------------------
