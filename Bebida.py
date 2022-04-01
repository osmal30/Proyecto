from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, inventario, tamano=None) -> None:
        self.inventario = [int(inventario/3)]*3
        super().__init__(nombre, precio, inventario)
        self.tamano = tamano        
        self.tipo = 2
    
    def __str__(self) -> str:
        prod = '''nombre: {}
precio: {}
tipo: {}'''
        if self.tipo == 1:
            return prod.format(self.nombre,self.precio,"Alimento")
        else:
            return prod.format(self.nombre,self.precio,"Bebida")
    