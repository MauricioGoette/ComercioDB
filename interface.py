from data_access import DataAccess
from tabulate import tabulate

class Interface:

    def __init__(self):
        self.datos = DataAccess() 

    ################################################ Clientes ######################################################

    # Mostrar clientes
    def mostrar_clientes(self):
        # lee los clientes
        clientes = self.datos.devolver_clientes()
        # Muestra el resultado
        print(tabulate(clientes, headers=['Cuit', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'ID']))
        # Espera un a tecla para salir
        input()

    #Clientes ordenados
    def mostrar_clientes_ordenados(self):
        print(" 1-Id \n 2-Nombre \n 3-Apellido \n")
        seleccion = input('Seleccione el tipo de orden: ')
 
        if seleccion == '1':
            orden = 'id_cliente desc'
        elif seleccion == '2':
            orden = "nombre_cliente"
        elif seleccion == '3':
            orden = "apellido_cliente"
        else:
            print("Opcion erronea")

        print(orden)
        clientes = self.datos.devolver_clientes_ordenados(orden)

        print(tabulate(clientes, headers=['Cuit', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'ID']))           
        input()

    #Buscar cliente por nombre
    def buscar_clientes_nombre(self):
        if self.datos.conectado():
            nombre = input('Nombre del cliente: ')
            clientes = self.datos.devolver_clientes_nombre(nombre)
            print(tabulate(clientes, headers=['Cuit', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'Id']))
        else:
            print('No conectado')
        input()

    #Buscar clientes por apellido
    def buscar_clientes_apellido(self):
        if self.datos.conectado():
            apellido = input('Apellido del cliente: ')
            clientes = self.datos.devolver_clientes_apellido(apellido)
            print(tabulate(clientes, headers=['Cuit', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'Id']))
        else:
            print('No conectado')
        input()
    
    # Agregar cliente
    def agregar_cliente(self):
        if self.datos.conectado():
            cuit= input('Cuit: ')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            rsocial = input('Razon social: ')
            direccion = input('Direccion: ')
            telefono = input('Telefono: ')
            # intenta insertar una nueva banda
            if self.datos.agregar_cliente(cuit, nombre, apellido, rsocial, direccion, telefono):
                print('\n','Cliente ingresado correctamente')
        else:
            print('No conectado')
        # Espera un a tecla para salir
        input()

    # Modificar cliente
    def editar_cliente(self):
        if self.datos.conectado():
            clientes = self.datos.devolver_clientes()
            print(tabulate(clientes, headers=['Cuit', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'ID']))
            print()
            id = input('Seleccione el id del cliente a editar: ')
            cuit= input('Cuit: ')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            rsocial = input('Razon social: ')
            direccion = input('Direccion: ')
            telefono = input('Telefono: ')
            # Ejecuta una consulta
            if self.datos.editar_cliente(id, cuit, nombre, apellido, rsocial, direccion, telefono):
                print('\n', 'Cliente actualizado')
        else:
            print('No conectado')
        input()

    

    ################################################ Proveedores ######################################################

    #Mostrar proveedores
    def mostrar_proveedores(self):
        # lee los proveedores
        proveedores = self.datos.devolver_proveedores()
        # Muestra el resultado
        print(tabulate(proveedores, headers=['Cuit', 'Nombre', 'Telefono', 'Direccion', 'Mail', 'CBU', 'Cotizacion Dolar', 'ID', 'Estado']))
        # Espera un a tecla para salir
        input()

    # Agregar proveedor
    def agregar_proveedor(self):
        if self.datos.conectado():
            cuit= input('Cuit: ')
            nombre = input('Nombre: ')
            telefono = input('Telefono: ')
            direccion = input('Direccion: ')
            mail = input('Mail: ')
            cbu = input('Cbu: ')
            dolar = input('Valor del dolar: ')
            if self.datos.agregar_proveedor(cuit, nombre, telefono, direccion, mail, cbu, dolar):
                print('\n','Proveedor ingresado correctamente')
        else:
            print('No conectado')
        # Espera un a tecla para salir
        input()

    # Modificar dolar proveedor
    def modificar_dolar(self):
        if self.datos.conectado():
            proveedores = self.datos.devolver_proveedores()
            num_proveedores = list(proveedores)
            for i in range(0, len(num_proveedores)):
                proveedor = list(num_proveedores[i])
                proveedor[0] = i+1
                num_proveedores[i] = tuple(proveedor)
            print(tabulate(num_proveedores, headers=['Nombre', 'Telefono', 'Direccion', 'Mail', 'CBU', 'Cotizacion Dolar', 'Id', 'Estado']))
            print()
            num = input('Seleccione el número del proveedor a modificar dolar: ')
            proveedor_id = proveedores[int(num)-1][0]
            valor = input('Valor del dolar: ')
            if self.datos.modificar_dolar(valor, proveedor_id):
                print('\n', 'Valor actualizado')
        else:
            print('No conectado')
        input()

    # Modificar estado proveedor
    def modificar_estado(self):
        if self.datos.conectado():
            proveedores = self.datos.devolver_proveedores()
            num_proveedores = list(proveedores)
            for i in range(0, len(num_proveedores)):
                proveedor = list(num_proveedores[i])
                proveedor[0] = i+1
                num_proveedores[i] = tuple(proveedor)
            print(tabulate(num_proveedores, headers=['Nombre', 'Telefono', 'Direccion', 'Mail', 'CBU', 'Cotizacion Dolar', 'Id', 'Estado']))
            print()
            num = input('Seleccione el número del proveedor a cambiar de estado: ')
            proveedor_id = proveedores[int(num)-1][0]
            print("\n 1-Activo \n 2-Inactivo")
            estado = input('Seleccione el Estado \n Opcion: ')

            if estado == '1':
                estado = 'A'
            elif estado == '2':
                estado = "I"
            else:
                print("Opcion erronea")

            if self.datos.modificar_estado(estado, proveedor_id):
                print('\n', 'Estado actualizado')
        else:
            print('No conectado')
        input()

    ################################################ Productos ######################################################

    # Productos Comerciados
    def mostrar_productos(self):
        productos = self.datos.devolver_productos()
        print(tabulate(productos, headers=['Id', 'Nombre', 'Codigo', 'Precio venta1(Menor Ganancia)', 'Precio venta2(Media Ganancia)', 'Precio venta3(Maxima Ganancia)', 'Proveedor']))
        input()

    # Agregar producto
    def agregar_producto(self):
        if self.datos.conectado():
            proveedores = self.datos.devolver_proveedores()
            num_proveedores = list(proveedores)
            for i in range(0, len(num_proveedores)):
                proveedor = list(num_proveedores[i])
                proveedor[0] = i+1
                num_proveedores[i] = tuple(proveedor)
            print(tabulate(num_proveedores, headers=['Nombre', 'Telefono', 'Direccion', 'Mail', 'CBU', 'Cotizacion Dolar', 'Id', 'Estado']))
            print()
            num = input('Seleccione el número del proveedor del producto: ')
            cuit_proveedor = proveedores[int(num)-1][0]

            nombre_producto = input('Nombre del producto: ')
            descripcion_producto = input('Descripcion: ')
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            categoria = input('Categoria: ')
            codigo = input('Codigo: ')
            precio_compra = input('Precio de compra(dolar): ')
            meses_garantia = input('Meses de garantia: ')
            if self.datos.agregar_producto(cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, meses_garantia):
                print('\n','Producto ingresado correctamente')
        else:
            print('No conectado')
        # Espera un a tecla para salir
        input()

    #Modificar ganancia de productos
    def modificar_ganancia(self):
        if self.datos.conectado():
            num = input('Seleccione la ganancia sobre los productos (0-100 %): ')
            if self.datos.modificar_ganancia(num):
                print('\n', 'Ganancia actualizada a {0} %'.format(num))
        else:
            print('No conectado')
        input()

    # Buscar productos
    def buscar_productos(self):
        if self.datos.conectado():
            nombre = input('Nombre del producto: ')
            productos = self.datos.buscar_productos(nombre)
            print(tabulate(productos, headers=['Id', 'Nombre', 'Descripcion', 'Categoria', 'Codigo', 'Precio Venta(Pesos)']))
        else:
            print('No conectado')
        input()

    # Productos stock
    def mostrar_stock(self):
        stock = self.datos.devolver_stock()
        print(tabulate(stock, headers=['Id', 'Nombre', 'Cantidad en stock']))
        input()


    ################################################ Ventas ######################################################
    
    #Mostrar ventas
    def mostrar_ventas(self):
        venta = self.datos.devolver_ventas()
        print(tabulate(venta, headers=['Id', 'Fecha', 'Nombre', 'Apellido', 'Razon social', 'Producto', "Precio unitario(Pesos)", 'Cantidad', 'Total(Pesos)']))
        input()

    #Agregar venta
    def agregar_venta(self):
        if self.datos.conectado():
            #Buscar cliente por apellido        
            apellido = input('Apellido del cliente: ')            
            clientes = self.datos.devolver_clientes_apellido(apellido)
            num_clientes = list(clientes)
            for i in range(0, len(num_clientes)):
                cliente = list(num_clientes[i])
                cliente[0] = i+1
                num_clientes[i] = tuple(cliente)
            print(tabulate(num_clientes, headers=['Id(Lista)', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'Id(BDD)']))
            print()
            num = input('Seleccione el Id(Lista) del cliente: ')
            cuit = clientes[int(num)-1][0]

            fecha = input('Fecha(YYYY-MM-DD): ')
            
            #Busqueda y seleccion del producto a vender
            nombre = input('Buscar producto: ')
            productos = self.datos.buscar_productos(nombre)
            num_productos = list(productos)
            for i in range(0, len(num_productos)):
                producto = list(num_productos[i])
                producto[0] = i+1
                num_productos[i] = tuple(producto)
            print(tabulate(num_productos, headers=['Id', 'Nombre', 'Descripcion', 'Categoria', 'Codigo', 'Precio Venta(Pesos)']))
            print()
            num2 = input('Seleccione el Id del producto a vender: ')
            id_producto = productos[int(num2)-1][0]

            cantidad = input('Cantidad: ')
            
            if self.datos.agregar_venta(cuit, fecha, id_producto, cantidad):
                print('\n','Venta agregada correctamente')
        else:
            print('No conectado')
        # Espera un a tecla para salir
        input()

    #Misma Venta
    def misma_venta(self):
        if self.datos.conectado():
            #Busqueda y seleccion del producto a vender
            nombre = input('Buscar producto: ')
            productos = self.datos.buscar_productos(nombre)
            num_productos = list(productos)
            for i in range(0, len(num_productos)):
                producto = list(num_productos[i])
                producto[0] = i+1
                num_productos[i] = tuple(producto)
            print(tabulate(num_productos, headers=['Id', 'Nombre', 'Descripcion', 'Categoria', 'Codigo', 'Precio Venta(Pesos)']))
            print()
            num2 = input('Seleccione el Id del producto(distinto) a vender: ')
            id_producto = productos[int(num2)-1][0]
            
            cantidad = input('Cantidad: ')
            
            if self.datos.misma_venta(id_producto, cantidad):
                print('\n','Venta agregada correctamente')
        else:
            print('No conectado')
        input()    

    ################################################ Servicios ######################################################

    #Mostrar servicios
    def mostrar_servicios(self):
        servicio= self.datos.devolver_servicios()
        print(tabulate(servicio, headers=['Id', 'Fecha', 'Nombre', 'Apellido', 'Password', 'Descripcion', 'Cantidad', 'Total']))
        input()

    #Agregar servicio
    def agregar_servicio(self):
        if self.datos.conectado():
            #Buscar cliente por apellido        
            apellido = input('Apellido del cliente: ')            
            clientes = self.datos.devolver_clientes_apellido(apellido)
            num_clientes = list(clientes)
            for i in range(0, len(num_clientes)):
                cliente = list(num_clientes[i])
                cliente[0] = i+1
                num_clientes[i] = tuple(cliente)
            print(tabulate(num_clientes, headers=['Id(Lista)', 'Nombre', 'Apellido', 'Razon Social', 'Direccion', 'Telefono', 'Id(BDD)']))
            print()
            num = input('Seleccione el Id(Lista) del cliente: ')
            cuit = clientes[int(num)-1][0]


            fecha = input('Fecha(YYYY-MM-DD): ')
            descripcion = input('Descripcion del servicio: ')
            contrasenia = input('Password (En blanco:default): ')
            cantidad = input('Cantidad: ')
            total = input('Total: ')
            
            if self.datos.agregar_servicio(cuit, fecha, descripcion, contrasenia, cantidad, total):
                print('\n','Servicio agregado correctamente')
        else:
            print('No conectado')
        # Espera un a tecla para salir
        input()

    #Mismo servicio
    def mismo_servicio(self):
        if self.datos.conectado():
            descripcion = input('Descripcion del servicio: ')
            cantidad = input('Cantidad: ')
            total = input('Total: ')
            
            if self.datos.mismo_servicio(descripcion, cantidad, total):
                print('\n','Servicio agregado correctamente')
        else:
            print('No conectado')
        input()    


    ################################################ Compras ######################################################

    #Mostrar compras
    def mostrar_compras(self):
        servicio= self.datos.devolver_compras()
        print(tabulate(servicio, headers=['Id Compra', 'Proveedor', 'Fecha', 'Producto', 'Cantidad', 'Precio/unidad', 'Total']))
        input()

    #Agregar compra
    def agregar_compra(self):
        if self.datos.conectado():
            proveedores = self.datos.devolver_proveedores()
            num_proveedores = list(proveedores)
            for i in range(0, len(num_proveedores)):
                proveedor = list(num_proveedores[i])
                proveedor[0] = i+1
                num_proveedores[i] = tuple(proveedor)
            print(tabulate(num_proveedores, headers=['Nombre', 'Telefono', 'Direccion', 'Mail', 'CBU', 'Cotizacion Dolar', 'Id', 'Estado']))
            print()
            num = input('Seleccione el número del proveedor donde realizar la compra: ')
            proveedor_id = proveedores[int(num)-1][0]
            fecha = input('Fecha(YYYY-MM-DD): ')

            #Busqueda y seleccion del producto a comprar
            nombre = input('Buscar producto: ')
            productos = self.datos.buscar_productos(nombre)
            num_productos = list(productos)
            for i in range(0, len(num_productos)):
                producto = list(num_productos[i])
                producto[0] = i+1
                num_productos[i] = tuple(producto)
            print(tabulate(num_productos, headers=['Id', 'Nombre', 'Descripcion', 'Categoria', 'Codigo', 'Precio Venta(Pesos)']))
            print()

            
            ### test

            if len(num_productos) == 0:
                print("Producto no encontrado / Ingresar Producto")
                
                cuit_proveedor = proveedor_id
                nombre_producto = input('Nombre del producto: ')
                descripcion_producto = input('Descripcion: ')
                marca = input('Marca: ')
                modelo = input('Modelo: ')
                categoria = input('Categoria: ')
                codigo = input('Codigo: ')
                precio_compra = input('Precio de compra(dolar): ')
                meses_garantia = input('Meses de garantia: ')
                if self.datos.agregar_producto(cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, meses_garantia):
                    print('\n','Producto ingresado correctamente')
                
                cantidad = input('Cantidad: ')
                precio_unitario = precio_compra
                id_producto = self.datos.devolver_lastIdProducto()
                

                if self.datos.agregar_compra(proveedor_id, fecha, cantidad, id_producto, precio_unitario):
                    print('\n','Nueva compra generada correctamente')

                        
            else:
                num2 = input('Seleccione el Id del producto a comprar: ')
                id_producto = productos[int(num2)-1][0]

                cantidad = input('Cantidad: ')
                precio_unitario = input('Precio Unitario (Dolares): ')
                if self.datos.agregar_compra(proveedor_id, fecha, id_producto, cantidad, precio_unitario):
                    print('\n','Nueva compra generada correctamente')
                    
              
        else:
            print('No conectado')
        input()

    #Misma compra
    def misma_compra(self):
        if self.datos.conectado():
            #Busqueda y seleccion del producto a comprar
            nombre = input('Buscar producto(Diferente al ultimo ingresado): ')
            productos = self.datos.buscar_productos(nombre)
            num_productos = list(productos)
            for i in range(0, len(num_productos)):
                producto = list(num_productos[i])
                producto[0] = i+1
                num_productos[i] = tuple(producto)
            print(tabulate(num_productos, headers=['Id', 'Nombre', 'Descripcion', 'Categoria', 'Codigo', 'Precio Venta(Pesos)']))
            print()

            ## test2
            if len(num_productos) == 0:
                print("Producto no encontrado / Ingresar Producto")
                
                cuit_proveedor = self.datos.devolver_lastProveedor()
                nombre_producto = input('Nombre del producto: ')
                descripcion_producto = input('Descripcion: ')
                marca = input('Marca: ')
                modelo = input('Modelo: ')
                categoria = input('Categoria: ')
                codigo = input('Codigo: ')
                precio_compra = input('Precio de compra(dolar): ')
                meses_garantia = input('Meses de garantia: ')
                if self.datos.agregar_producto(cuit_proveedor, nombre_producto, descripcion_producto, marca, modelo, categoria, codigo, precio_compra, meses_garantia):
                    print('\n','Producto ingresado correctamente')
                
                cantidad = input('Cantidad: ')
                precio_unitario = precio_compra
                id_producto = self.datos.devolver_lastIdProducto()
                

                if self.datos.misma_compra(id_producto, cantidad, precio_unitario):
                    print('\n','Compra agregada correctamente')

            else:
                num2 = input('Seleccione el Id del producto a comprar: ')
                id_producto = productos[int(num2)-1][0]

                cantidad = input('Cantidad: ')
                precio_unitario = input('Precio(Dolares): ')
                
                if self.datos.misma_compra(id_producto, cantidad, precio_unitario):
                    print('\n','Compra agregada correctamente')

        else:
            print('No conectado')
        input()    
       
    

        


    