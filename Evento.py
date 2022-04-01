from datetime import datetime
from Layout import Layout

class Evento:
   
    def __init__(self, title:str , type: int, cartel:list, general:Layout, vip: Layout, date: datetime, bands: int=-1, synopsys: str = ""):
        self.title:str = title
        self.type: int = type
        self.synopsys:str = synopsys
        self.bands: int = bands
        self.layout = {}
        self.layout["general"] = general
        self.layout["vip"] = vip
        self.cartel:list = cartel
        self.date: datetime = datetime.strptime(date,"%Y-%m-%d")
        self.type_name = {1: 'Musical', 2: 'Obra de teatro'}     
        self.ventas_abiertas = True
    
    def info_by_type(self) -> str:
        if self.type == 1:
            return 'bandas: {}'.format(self.bands)
        else:
            return 'sinopsis: {}'.format(self.synopsys) 

    def __str__(self) -> str:
        global info_by_type
        return ''' Nombre del Evento: {}
    Tipo: {}
    {}
    Cartel: {}
    Fecha: {}
    Asientos: 
        General: {}$
        VIP: {}$
    '''.format(self.title,self.type_name[self.type], self.info_by_type(), ', '.join(self.cartel), self.date.strftime("%d/%m/%Y"), self.layout["general"].precio, self.layout["vip"].precio)

    def layout_info(self):
        informacion = "General\n"
        informacion +=str(self.layout["general"])
        informacion += "\nVIP\n"
        informacion +=str(self.layout["vip"])
        return informacion

    def cambiar_estado_ventas(self):
        self.ventas_abiertas = not self.ventas_abiertas
        if self.ventas_abiertas:
            print('Se abrieron las ventas del evento {}'.format(self.title))
        else:
            print('Se cerraron las ventas del evento {}'.format(self.title))