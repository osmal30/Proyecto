from cmath import inf
from datetime import datetime


def leer_entero(mensaje:str, l_inf:int=0, l_sup:int = inf)->int:    
    while True:
        try:
            opcion= int(input(mensaje+"\n Indique su opcion "))
            if l_inf <= opcion <= l_sup:
                break
            print("valor inválido")
        except:
            print("valor inválido")
    return opcion

def leer_fecha(mensaje:str, formato:str)->datetime:
    while True:
        try:
            fecha_str = input(mensaje)
            fecha = datetime.strptime(fecha_str, formato)
            return fecha;'[ '
        except:
            print("Fecha inválida")