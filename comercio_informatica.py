'''
    Instalar paquetes usados:
        pip install console-menu    - Para crear el menu
        pip install tabulate        - Para mostrar los resultados en forma de tabla
        pip install psycopg2        - adapter para conectarse a PostgreSQL (wrapper de la libreria libpq) 

        python -m pip install console-menu....
'''



# Importa los paquetes para crear un menu
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem

from interface import Interface



def menu():

    ### Sub-submenu Buscar Clientes
    submenu_buscar_clientes = ConsoleMenu(title="Buscar Clientes", exit_option_text='Volver')
    submenu_buscar_clientes.append_item(FunctionItem("Buscar clientes por nombre", interface.buscar_clientes_nombre))
    submenu_buscar_clientes.append_item(FunctionItem("Buscar clientes por apellido", interface.buscar_clientes_apellido))

    ### Sub-submenu Mostrar Clientes
    submenu_mostrar_clientes = ConsoleMenu(title="Mostrar Clientes", exit_option_text='Volver')
    submenu_mostrar_clientes.append_item(FunctionItem("Mostrar Todos los clientes", interface.mostrar_clientes))
    submenu_mostrar_clientes.append_item(FunctionItem("Mostrar clientes por orden", interface.mostrar_clientes_ordenados))
    
    ## Submenu Clientes
    submenu_clientes = ConsoleMenu(title="Clientes", exit_option_text='Volver')
    submenu_clientes.append_item(SubmenuItem("Mostrar Clientes", submenu=submenu_mostrar_clientes))
    submenu_clientes.append_item(SubmenuItem("Buscar cliente", submenu=submenu_buscar_clientes))
    submenu_clientes.append_item(FunctionItem("Agregar cliente", interface.agregar_cliente))
    submenu_clientes.append_item(FunctionItem("Editar cliente", interface.editar_cliente))
    
      
    ## Submenu Proveedores
    submenu_proveedores = ConsoleMenu(title="Proveedores", exit_option_text='Volver')
    submenu_proveedores.append_item(FunctionItem("Mostrar Proveedores", interface.mostrar_proveedores))
    submenu_proveedores.append_item(FunctionItem("Agregar Proveedor", interface.agregar_proveedor))
    submenu_proveedores.append_item(FunctionItem("Modificar Dolar Proveedor", interface.modificar_dolar))
    submenu_proveedores.append_item(FunctionItem("Modificar Estado Proveedor", interface.modificar_estado))
    
    ## Submenu Productos
    submenu_productos = ConsoleMenu(title="Productos ", exit_option_text='Volver')
    submenu_productos.append_item(FunctionItem("Mostrar productos comerciados", interface.mostrar_productos))
    submenu_productos.append_item(FunctionItem("Agregar producto", interface.agregar_producto))
    submenu_productos.append_item(FunctionItem("Modificar Ganancia", interface.modificar_ganancia))
    submenu_productos.append_item(FunctionItem("Buscar producto", interface.buscar_productos))
    submenu_productos.append_item(FunctionItem("Mostrar Stock", interface.mostrar_stock))
    
    ## Submenu Ventas
    submenu_ventas = ConsoleMenu(title="Ventas", exit_option_text='Volver')
    submenu_ventas.append_item(FunctionItem("Mostrar ventas", interface.mostrar_ventas))
    submenu_ventas.append_item(FunctionItem("Nueva venta", interface.agregar_venta))
    submenu_ventas.append_item(FunctionItem("Agregar Productos a ultima venta", interface.misma_venta))

    ## Submenu Servicios
    submenu_servicios = ConsoleMenu(title="Servicios", exit_option_text='Volver')
    submenu_servicios.append_item(FunctionItem("Mostrar servicios", interface.mostrar_servicios))
    submenu_servicios.append_item(FunctionItem("Nuevo servicio", interface.agregar_servicio))
    submenu_servicios.append_item(FunctionItem("Agregar al ultimo servicio", interface.mismo_servicio))

    ## Submenu Compras
    submenu_compras = ConsoleMenu(title="Compras", exit_option_text='Volver')
    submenu_compras.append_item(FunctionItem("Mostrar compras", interface.mostrar_compras))
    submenu_compras.append_item(FunctionItem("Nueva compra", interface.agregar_compra))
    submenu_compras.append_item(FunctionItem("Agregar a la compra", interface.misma_compra))

    # Crea el menu principal
    menu_principal = ConsoleMenu("Comercio de Informatica - Mauricio Goette", ("NO conectado" if not interface.datos.conectado() else "Conectado") +  " a la base de datos", exit_option_text='Salir')
    menu_principal.append_item(SubmenuItem("Clientes", submenu=submenu_clientes))
    menu_principal.append_item(SubmenuItem("Proveedores", submenu=submenu_proveedores))
    menu_principal.append_item(SubmenuItem("Productos", submenu=submenu_productos))
    menu_principal.append_item(SubmenuItem("Ventas", submenu=submenu_ventas))
    menu_principal.append_item(SubmenuItem("Servicios", submenu=submenu_servicios))
    menu_principal.append_item(SubmenuItem("Compras", submenu=submenu_compras))
    

    # Muestra el menu
    menu_principal.show()


if __name__ == "__main__":
    # Crea un objeto del tipo Reproductor
    interface = Interface()

    menu()

    