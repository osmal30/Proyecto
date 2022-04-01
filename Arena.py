from datetime import datetime
from Entrada import Entrada
import funciones
from Alimento import Alimento
from Bebida import Bebida
from Layout import Layout
from Evento import Evento
class Arena:
    def __init__(self) -> None:
        self.eventos:list = []
        self.clientes:dict = {}
        self.productos:list = []
        self.facturas= {"entradas":[],"productos":[]}

    
    def agregar_evento(self, diccionario:dict):
        general: Layout = Layout(diccionario["layout"]["general"][0], diccionario["layout"]["general"][1], diccionario["prices"][0])        
        vip: Layout = Layout(diccionario["layout"]["vip"][0], diccionario["layout"]["vip"][1], diccionario["prices"][1])        
        if diccionario["type"] == 2:            
            evento = Evento(diccionario["title"],diccionario["type"],diccionario["cartel"],general, vip, diccionario["date"], None, diccionario["synopsis"])
        else:
            evento = Evento(diccionario["title"],diccionario["type"], diccionario["cartel"],general, vip, diccionario["date"],diccionario["bands"],None)
        self.eventos.append(evento)
    
    def listar_eventos_todos(self):
        return self.listar_eventos(self.eventos)
    def listar_eventos(self, lista:list):
        return '\n'.join('\nEvento {}:\n{}'.format(*k)for k in enumerate(lista, start=1))
    
    def listar_eventos_resumido(self)->str:
        return '\n'.join('\nEvento {}: {}'.format(k[0], k[1].title)for k in enumerate(self.eventos, start=1))
        
    def cambiar_estado_ventas(self, nro_ventas:int):
        self.eventos[nro_ventas].cambiar_estado_ventas()
    
    def buscar_tipo(self):
        menu = '''Seleccione el tipo de evento:
        1. Musical
        2. Obra de reatro'''
        tipo = funciones.leer_entero(menu,1,2)
        lista = filter(lambda evento:evento.type == tipo, self.eventos)
        print(self.listar_eventos(lista))

    def buscar_fecha(self):
        fecha = funciones.leer_fecha("Ingrese la fecha del evento (dd/mm/aaaa): ","%d/%m/%Y")
        lista = filter(lambda evento:evento.date == fecha, self.eventos)
        print(self.listar_eventos(lista))

    def buscar_cartel(self):
        nombre = input("Ingrese el nombre del actor/cantante: ")
        lista = filter(lambda evento: nombre in evento.cartel, self.eventos)
        print(self.listar_eventos(lista))

    def buscar_nombre(self):
        nombre = input("Ingrese el nombre del evento: ")
        lista = filter(lambda evento: evento.title==nombre, self.eventos)
        print(self.listar_eventos(lista))

    def agregar_alimento(self,food):
        if food["type"] == 1:
            producto = Alimento(food["name"], food["price"], food["amount"], food["presentation"])
        else:
            producto = Bebida(food["name"], food["price"], food["amount"])
        self.productos.append(producto) 
    
    def escoger_entradas(self,evento,cant_tickets):
        entradas= []
        for n in range(0,cant_tickets):
            mensaje= '''Seleccione el tipo de entrada
            1. General
            2. VIP'''
            tipo = funciones.leer_entero(mensaje,1,2)
            if tipo == 1:
                tablero = self.eventos[evento].layout["general"]
                tipo_str = "general"                
            else:
                tablero = self.eventos[evento].layout["vip"]
                tipo_str = "vip"
            fila = funciones.leer_entero("Ingrese la fila: ", 1,tablero.fila)
            columna = funciones.leer_entero("Ingrese la columna: ", 1,tablero.columna)
            entrada = Entrada(tipo_str,fila,columna,tablero.precio)
            entradas.append(entrada)
        return entradas
    def reservar_entradas(self,evento,tickets):
        for entrada in tickets:
            self.eventos[evento].layout[entrada.tipo].asientos[entrada.fila-1][entrada.columna-1] = True

    def buscar_producto_nombre(self):
        nombre = input("Ingrese el nombre del producto")
        lista = filter(lambda producto:producto.nombre == nombre, self.productos)
        print(self.listar_productos(lista))
    
    def buscar_producto_tipo(self):
        mensaje = "Ingrese 1. para alimento, 2. para bebida: "
        tipo = funciones.leer_entero(mensaje, 1,2)    
        lista = filter(lambda producto:producto.tipo == tipo, self.productos)        
        print(self.listar_productos(lista))
    def buscar_producto_precio(self):
        lim_inferior = funciones.leer_entero("Ingrese el limite inferior")
        lim_superior = funciones.leer_entero("Ingrese el limite superior",lim_inferior)
        lista = []
        for producto in self.productos:
            if isinstance(producto,Alimento):
                if lim_inferior<= producto.precio <= lim_superior:
                    lista.append(producto)
            else:
                if (lim_inferior<= producto.precio[0] <= lim_superior) or (lim_inferior<= producto.precio[1] <= lim_superior) or (lim_inferior<= producto.precio[2] <= lim_superior):
                    lista.append(producto)
        print(lista, sep="\n")
                
    def listar_productos(self, lista):
        return '\n'.join('\nEvento {}:\n{}'.format(*k)for k in enumerate(lista, start=1))
    
    def mostrar_mapa(self,indice):
        print(self.eventos[indice].layout_info())
    
    def mostrar_productos(self):
        return '\n'.join('\nProducto {}:\n{}'.format(*k)for k in enumerate(self.productos, start=1))
    
    def eliminar_producto(self, nro_producto):
        self.productos.pop(nro_producto)