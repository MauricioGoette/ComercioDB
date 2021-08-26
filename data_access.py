# Importar el paquete 
import psycopg2


class DataAccess:

    ###Conexion###
    def __init__(self):
        try:
            self.connection = None

            # Establece la conexión con el servidor
            self.connection = psycopg2.connect(user = "postgres",
                                      password = "elgranKathogas3",
                                      host = "localhost",
                                      port = "5432",
                                      database = "comerciodb")
            # Realiza un commit automaticamente
            self.connection.autocommit = True
            # Crea un cursor para poder realizar operaciones
            self.cursor = self.connection.cursor()

            print("Conexión exitosa con PostgreSQL")

        except (Exception, psycopg2.Error) as error :
            print ("Error al conectarse con PostgreSQL", error)
        
    def __del__(self):
        if (self.connection != None):
            # Cierra las conexiones
            self.cursor.close()
            self.connection.close()
            print("Conexión cerrada")


    def conectado(self):
                return self.connection != None and self.connection.closed == 0 
        
    ################################################ Clientes ######################################################

    # Mostrar clientes
    def devolver_clientes(self):
        if self.conectado():
            # Ejecuta una consulta
            self.cursor.execute('select * from cliente')
            # trae todo el resultado
            clientes = self.cursor.fetchall() 
            # retorna las bandas
            return clientes
        else:
            return []

    #Clientes ordenados
    def devolver_clientes_ordenados(self, orden):
        if self.conectado():
            try:
                sql = "select * from cliente order by {0}".format(orden)
                self.cursor.execute(sql)
                clientes = self.cursor.fetchall() 
                return clientes
                
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al ordenar ", '\n\t', error)
                return False
        else:
            return False

    #Buscar cliente por nombre
    def devolver_clientes_nombre(self, nombre):
        if self.conectado():
            self.cursor.execute("select * from buscar_cliente_nombre('{0}')".format(nombre))
            clientes  = self.cursor.fetchall()
            return clientes
        else:
            return []

    #Buscar cliente por apellido
    def devolver_clientes_apellido(self, apellido):
        if self.conectado():
            self.cursor.execute("select * from buscar_cliente_apellido('{0}')".format(apellido))
            clientes  = self.cursor.fetchall()
            return clientes
        else:
            return []
            

    # Agregar cliente
    def agregar_cliente(self, cuit, nombre, apellido, rsocial, direccion, telefono):
        if self.conectado():
            # Ejecuta una consulta
            try:
                sql = "call agregar_cliente ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(cuit, nombre, apellido, rsocial, direccion, telefono)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al insertar cliente:", '\n\t', error)
                return False
        else:
            return False

    # Modificar cliente
    def editar_cliente(self, id, cuit, nombre, apellido, rsocial, direccion, telefono):
        if self.conectado():
            try:
                self.cursor.execute("CALL actualizar_cliente ({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(id, cuit, nombre, apellido, rsocial, direccion, telefono))
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al editar cliente:", '\n\t', error)
                return False
        else:
            print('No conectado')
            return False
       



    ################################################ Proveedores ######################################################
    
    # Mostrar proveedores
    def devolver_proveedores(self):
        if self.conectado():
            # Ejecuta una consulta
            self.cursor.execute('select * from proveedor order by proveedor_id ')
            # trae todo el resultado
            proveedores = self.cursor.fetchall() 
            # retorna los proveedores
            return proveedores
        else:
            return [] 

    # Agregar proveedor
    def agregar_proveedor(self, cuit, nombre, telefono, direccion, mail, cbu, dolar):
        if self.conectado():
            # Ejecuta una consulta
            try:
                sql = "call agregar_proveedor ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6})".format(cuit, nombre, telefono, direccion, mail, cbu, dolar)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al insertar proveedor:", '\n\t', error)
                return False
        else:
            return False      

    # Modificar dolar proveedor
    def modificar_dolar(self, valor, proveedor_id):
        if self.conectado():
            try:
                sql = "update proveedor set dolar_proveedor = {0} where cuit_proveedor = '{1}' ".format( valor, proveedor_id)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al modificar el valor:", '\n\t', error)
                return False
        else:
            return False

    # Modificar estado proveedor
    def modificar_estado(self, estado, proveedor_id):
        if self.conectado():
            try:
                sql = "update proveedor set proveedor_status = '{0}' where cuit_proveedor = '{1}'".format(estado , proveedor_id)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al modificar el estado:", '\n\t', error)
                return False
        else:
            return False
    

    ################################################ Productos ######################################################

    # Productos Comerciados
    def devolver_productos(self):
        if self.conectado():
            self.cursor.execute('select distinct p.id_producto, p.descripcion_producto, p.codigo, multiplicar(p.precio_venta1, p2.dolar_proveedor), multiplicar(p.precio_venta2, p2.dolar_proveedor), multiplicar(p.precio_venta3, p2.dolar_proveedor), p2.nombre_proveedor from producto p, proveedor p2 where p.cuit_proveedor = p2.cuit_proveedor order by p.id_producto')
            productos = self.cursor.fetchall()
            return productos
        else:
            return []

    # Agregar producto
    def agregar_producto(self, cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, meses_garantia):
        if self.conectado():
            # Ejecuta una consulta
            try:
                sql = "call agregar_producto('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', {7}, {8})".format(cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, meses_garantia)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al insertar producto:", '\n\t', error)
                return False
        else:
            return False      

    #Modificar ganancia de productos
    def modificar_ganancia(self, ganancia):
        if self.conectado():
            try:
                sql = "update producto set precio_venta1 = (precio_compra * {0} / 100) + precio_compra".format(ganancia)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al modificar ganancia:", '\n\t', error)
                return False
        else:
            return False

    #Buscar producto
    def buscar_productos(self, nombre):
        if self.conectado():
            self.cursor.execute("select * from buscar_producto ('{0}')".format(nombre))
            productos  = self.cursor.fetchall()
            return productos
        else:
            return [] 

    #Obtener ultimo Id_producto
    def devolver_lastIdProducto(self):
        if self.conectado():
            self.cursor.execute("SELECT MAX(p.id_producto) FROM producto p")
            lastId_producto  = self.cursor.fetchone()[0]
            return lastId_producto
        else:
            return []

    # Productos stock
    def devolver_stock(self):
        if self.conectado():
            self.cursor.execute('select distinct p.id_producto, p.nombre_producto, i.stock_producto from producto p join inventario i on i.id_producto = p.id_producto ')
            stock = self.cursor.fetchall()
            return stock
        else:
            return []
    

    ################################################ Ventas ######################################################
    
    #Mostrar ventas
    def devolver_ventas(self):
        if self.conectado():
            self.cursor.execute('select * from orden_venta')
            ventas = self.cursor.fetchall()
            return ventas
        else:
            return []

    # Agregar venta
    def agregar_venta(self, cuit, fecha, id_producto, cantidad):
        if self.conectado():
            # Ejecuta una consulta
            try:
                sql = "call agregar_venta ('{0}', '{1}', {2}, {3})".format(cuit, fecha, id_producto, cantidad)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al insertar venta:", '\n\t', error)
                return False
        else:
            return False

    # Misma venta
    def misma_venta(self, id_producto, cantidad):
        if self.conectado():
            try:
                sql = "call misma_venta ({0}, {1})".format(id_producto, cantidad)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                print ('\n', "Error al insertar venta:", '\n\t', error)
                return False
        else:
            return False
                  

    ################################################ Servicios ######################################################
    
    #Mostrar servicios
    def devolver_servicios(self):
        if self.conectado():
            self.cursor.execute('select * from orden_servicio')
            servicios = self.cursor.fetchall()
            return servicios
        else:
            return []

    # Agregar servicio
    def agregar_servicio(self, cuit, fecha, descripcion, contrasenia, cantidad, total):
        if self.conectado():
            # Ejecuta una consulta
            try:
                sql = "call agregar_servicio ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(cuit, fecha, descripcion, contrasenia, cantidad, total)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al insertar servicio:", '\n\t', error)
                return False
        else:
            return False

    # Mismo servicio
    def mismo_servicio(self, descripcion, cantidad, total):
        if self.conectado():
            try:
                sql = "call mismo_servicio ('{0}', {1}, {2})".format(descripcion, cantidad, total)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                print ('\n', "Error al agregar servicio:", '\n\t', error)
                return False
        else:
            return False


    ################################################ Compras ######################################################

    #Mostrar compras
    def devolver_compras(self):
        if self.conectado():
            self.cursor.execute('select * from ver_compras_detalle')
            servicios = self.cursor.fetchall()
            return servicios
        else:
            return []

    #Agregar compra
    def agregar_compra(self, cuit, fecha, id_producto, cantidad, precio_unitario):
        if self.conectado():
            try:
                sql = "call agregar_compra ('{0}', '{1}', {2}, {3}, {4})".format(cuit, fecha, id_producto, cantidad, precio_unitario)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                # Mensaje de Error
                print ('\n', "Error al generar nueva compra:", '\n\t', error)
                return False
        else:
            return False

    # Misma compra
    def misma_compra(self, id_producto, cantidad, precio_unitario):
        if self.conectado():
            try:
                sql = "call misma_compra ({0}, {1}, {2})".format(id_producto, cantidad, precio_unitario)
                self.cursor.execute(sql)
                return True
            except (Exception, psycopg2.Error) as error :
                print ('\n', "Error al agregar a la compra:", '\n\t', error)
                return False
        else:
            return False

     #Obtener ultimo Id_producto
    def devolver_lastProveedor(self):
        if self.conectado():
            self.cursor.execute("SELECT MAX(p.cuit_proveedor) FROM producto p")
            lastProveedor = self.cursor.fetchone()[0]
            return lastProveedor
        else:
            return []