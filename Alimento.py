from Producto import Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, inventario, presentacion) -> None:        
        super().__init__(nombre, precio, inventario)
        self.tipo = 1
        self.presentacion = presentacion
    def __str__(self) -> str:
        prod = '''nombre: {}
precio: {}
tipo: {}'''
        if self.tipo == 1:
            return prod.format(self.nombre,self.precio,"Alimento")
        else:
            return prod.format(self.nombre,self.precio,"Bebida")
    