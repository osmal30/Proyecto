from Cliente import Cliente
from Evento import Evento
from Entrada import Entrada
import itertools


class Factura:
    def __init__(self, cliente:Cliente) -> None:
        self.cliente:Cliente = cliente       
        self.monto: float = 0.0
        self.descuento:float = 0.0        
        self.total = 0.0
        
        
    def calcular(self):
        None
    
    def calcular_monto(self):
        None

    def calcular_descuento(self):
        None

    def calcular_total(self):
        None
    
    def resumen(self):
        None