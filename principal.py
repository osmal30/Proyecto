
import requests
from Alimento import Alimento
from Bebida import Bebida
from Cliente import Cliente
from Factura import Factura
from Factura_Entrada import Factura_Entrada
from Producto import Producto
import funciones

from Arena import Arena

def cargar_estado_inicial():
    api:dict = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json').json()    

    for elemento in api["events"]:
        arena.agregar_evento(elemento)
    for food in api["food_fair_inventory"]:
        arena.agregar_alimento(food)
        

def ver_eventos():
    print(arena.listar_eventos_todos())

def ventana_tickets():
    nro_evento = funciones.leer_entero(arena.listar_eventos_resumido(), 1, len(arena.eventos))
    arena.cambiar_estado_ventas(nro_evento-1)

def buscar_evento():
    menu = '''Seleccione el tipo de busqueda:
    1. Tipo
    2. Fecha
    3. Actor/cantante en el cartel
    4. Nombre del evento
    5. Regresar al menu anterior'''
    while True:
        busqueda = funciones.leer_entero(menu, 1, 5)
        if busqueda == 1: 
            arena.buscar_tipo()
        elif busqueda == 2:
            arena.buscar_fecha()
        elif busqueda == 3:
            arena.buscar_cartel()
        elif busqueda == 4:
            arena.buscar_nombre()
        elif busqueda == 5:
            break


def gestion_eventos():
    menu='''
    1. Ver eventos
    2. Cerrar/Abrir venta de tickets
    3. Buscar eventos
    4. Volver al menú principal'''
    while True:
        opcion = funciones.leer_entero(menu,1, 4)
        if opcion == 1:
            ver_eventos()
        elif opcion == 2:
            ventana_tickets()
        elif opcion == 3:
            buscar_evento()
        else:
            break

def venta_tickets():
    nombre = input("Ingrese su nombre: ")
    cedula = funciones.leer_entero("Ingrese su cedula")
    edad = funciones.leer_entero("Igrese su edad", 0, 120)   
    if not cedula in arena.clientes.keys():
        cliente = Cliente(nombre,cedula,edad)
    else:
        cliente = arena.clientes[cedula]
    evento = funciones.leer_entero(arena.listar_eventos_todos(),1,len(arena.eventos))
    cant_tickets = funciones.leer_entero("Ingrese la cantidad de tickets que desea comprar",1)
    arena.mostrar_mapa(evento-1)
    tickets = arena.escoger_entradas(evento-1,cant_tickets)
    factura = Factura_Entrada(cliente,arena.eventos[evento-1],tickets)
    print(factura.resumen())
    pago = funciones.leer_entero("¿Desea proceder a pagar la entrada?\n1.Si\n2.no",1,2)
    if pago == 1:
        arena.reservar_entradas(evento-1,tickets)
        arena.clientes[cedula] = cliente
        arena.facturas["entradas"].append(factura)

def gestion_feria_comida():
    while True:
        menu = '''Seleccione la funcion que desea realizar:    
        1. eliminar producto
        2. buscar producto
        3. volver al menu anterior'''
        opcion = funciones.leer_entero(menu,1,3)
        if opcion == 1:
            eliminar_producto()
        elif opcion == 2:
            buscar_producto()
        else:
            break

def eliminar_producto():
    print("Selecciones el producto que desea eliminar")
    nro_producto= funciones.leer_entero (arena.mostrar_productos(), 1,len(arena.productos))
    arena.eliminar_producto(nro_producto-1)

def buscar_producto():
    menu = '''Seleccione el tipo de busqueda:
    1. Nombre
    2. Tipo
    3. Rango de precios    
    4. Regresar al menu anterior'''
    while True:
        busqueda = funciones.leer_entero(menu, 1, 5)
        if busqueda == 1: 
            arena.buscar_producto_nombre()
        elif busqueda == 2:
            arena.buscar_producto_tipo()
        elif busqueda == 3:
            arena.buscar_producto_precio()
        elif busqueda == 4:
            break

def venta_feria_comida():
    cedula = funciones.leer_entero("Ingrese la cedula ",0)
    if not cedula in arena.clientes.keys():
        print("Cedula no encontrada")
        return
    
    

def estadisticas():
    None

arena:Arena = Arena()

def main()->None:
    cargar_estado_inicial()
    menu:str = '''Bienvenidos a Saman Show
    1.  Módulo de gestión de eventos
    2.	Módulo de Ventas de tickets
    3.	Módulo de Gestión de Feria de comida
    4.	Modulo de Venta de Feria de comida
    5.	Módulo de Estadísticas
    6.  Salir'''
    while True:
        opcion:int = funciones.leer_entero(menu, 1, 6)

        if opcion == 1:
            gestion_eventos()
        elif opcion == 2:
            venta_tickets()
        elif opcion == 3:
            gestion_feria_comida()
        elif opcion == 4:
            venta_feria_comida()
        elif opcion == 5:
            estadisticas()
        else:
            print("Adios!!")
            break

main()