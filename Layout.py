import string
class Layout:
    def __init__(self, fila:int, columna:int, precio:float) -> None:
        self.fila:int =fila
        self.columna:int = columna
        self.precio:float = precio
        self.asientos = [[False]*columna]*fila
    
    def __str__(self) -> str:    
        convert = {True: 'X', False:'O'}
        return '  '+' '.join(string.ascii_uppercase[:self.columna]) + '\n' + '\n'.join('{} {}'.format(k[0], ' '.join('{}'.format(convert[j[1]]) for j in enumerate(k[1])) )for k in enumerate(self.asientos, start=1))

