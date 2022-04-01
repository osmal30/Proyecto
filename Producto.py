from mailbox import NoSuchMailboxError


class Producto:
    def __init__(self, nombre, precio, inventario) -> None:
        self.nombre = nombre        
        self.precio = precio
        self.inventario = inventario
        self.tipo = 0

    def __str__(self) -> str:
        prod = '''nombre: {}
precio: {}
tipo: {}'''
        if self.tipo == 1:
            return prod.format(self.nombre,self.precio,"Alimento")
        else:
            return prod.format(self.nombre,self.precio,"Bebida")
        
    def __repr__(self) -> str:
        return self.__str__()