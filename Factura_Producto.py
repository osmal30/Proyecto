import Factura
class Factura_Producto(Factura):
    def __init__(self,cliente, productos:list) -> None:
        super().__init__(cliente)
        self.productos = productos
        self.calcular()

    def calcular(self):
        self.calcular_monto()
        self.calcular_descuento()
        self.calcular_total()    
    
    def calcular_monto(self):
        for producto in self.productos:
            self.monto +=producto[1]

    def calcular_descuento(self):
        cedula_str = str(self.cliente.cedula)
        potencia = len(cedula_str)
        total = 0
        for digito in cedula_str:
            total += int(digito)**potencia
        if total == self.cliente.cedula:
            self.descuento = self.monto * 0.15


    def calcular_total(self):
        self.total = self.monto -self.descuento

    def resumen(self):
        informacion = "Resumen de compra"
        for producto in self.productos:
            informacion+="\n{} ${}".format(producto.nombre, producto[1])
        if self.descuento >0:
            informacion+= "\ndescuento: {}".format(self.descuento)
        informacion+="\ntotal: {}".format(self.total)