from Factura import Factura
from Evento import Evento
from Cliente import Cliente
import itertools

class Factura_Entrada(Factura):
    def __init__(self, cliente: Cliente, evento: Evento, entradas: list) -> None:
        super().__init__(cliente)
        self.evento:Evento = evento
        self.entradas:list = entradas
        self.iva:float = 0.0
        self.calcular()

    def calcular(self):
        self.calcular_monto()
        self.calcular_descuento()
        self.calcular_iva()
        self.calcular_total()

    def calcular_monto(self):
        for entrada in self.entradas:
            self.monto += self.evento.layout[entrada.tipo].precio

    def ordenar(self, cadena:str):
        lista = []
        lista[:0]=cadena
        lista.sort()
        return lista

    def calcular_descuento(self):
        cedula = self.cliente.cedula
        cedula_str = self.ordenar(str(cedula))
        if len(cedula_str)%2 != 0:
            return
        colmillo_size:int = int(len(cedula_str)/2)
        permutaciones = list(itertools.permutations(cedula_str,r=colmillo_size))
        combinaciones = list(itertools.permutations(range(len(permutaciones)),r=2))
        for combinacion in combinaciones:
            colmillo_1= ''.join(permutaciones[combinacion[0]])
            colmillo_2= ''.join(permutaciones[combinacion[1]])
            if colmillo_1[-1] == '0' and colmillo_2[-1] == '0':
                continue
            if int(colmillo_1) * int(colmillo_2) != cedula:
                continue
            if set(self.ordenar(colmillo_1+colmillo_2))==set(cedula_str):
                self.descuento = self.monto*0.5
                return
            
    def calcular_iva(self):
        self.iva = (self.monto - self.descuento)*0.16
    
    def calcular_total(self):
        self.total = self.monto -self.descuento + self.iva

    def resumen(self):
        informacion = "Resumen de compra" 
        for entrada in self.entradas:
            informacion += "\nentrada {}-{}{} ${}".format(entrada.tipo,entrada.fila,entrada.columna, entrada.precio)
        informacion+="\nsubtotal: {}".format(self.monto)
        if self.descuento >0:
            informacion+= "\ndescuento: {}".format(self.descuento)
        informacion+="\niva: {}".format(self.iva)
        informacion+="\ntotal: {}".format(self.total)
