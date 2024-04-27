from error import LargoExcedidoError
from datetime import date, datetime
from anuncio import *

class Campania():
    
    def __init__(self, nombre:str="Nombre por defecto", fecha_inicio:date=datetime(1900,1,1), fecha_termino:date=datetime(3000,12,31), anuncios:list=[]) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios =  anuncios 
    
    
        
    
    @property
    def nombre_campania(self):
        return self.__nombre
    
    @nombre_campania.setter
    def nombre_campania(self, nuevonombre_campania):
        try: 
            if len(nuevonombre_campania) > 250:
                raise LargoExcedidoError("Nombre de la campaña excede los 250 caracteres.")
            else:
                self.__nombre = nuevonombre_campania
        except LargoExcedidoError as e:
            print(e)
            print()
            exit()

    @property #esto es un getter y obtiene el valor de la variable privada del return
    def fecha_inicio(self):
        return self.__fecha_inicio 
    
    @fecha_inicio.setter #esto es un setter y asigna un valor a la variable privada (en este caso a fecha de inicio)
    def fecha_inicio(self, nuevafecha): 
        self.__fecha_inicio = nuevafecha 
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, nuevafecha):
        self.__fecha_termino = nuevafecha 
    
    @property
    def anuncios(self):
        return self.__anuncios
    
    def __str__(self) -> str: #muestra una respuesta de la clase segun nosotros la configuremos
        cantidad_de_anuncios={
            "video":0,
            "display":0,
            "social":0
        }
        
        for aviso in self.__anuncios:
            if isinstance(aviso,Video):
                cantidad_de_anuncios["video"]+=1
            elif isinstance(aviso,Display):
                cantidad_de_anuncios["display"]+=1
            elif isinstance(aviso,Social):
                cantidad_de_anuncios["social"]+=1
        
        mensaje=f"nombre de campaña:{self.__nombre}\nvideo:{cantidad_de_anuncios['video']}\tdisplay:{cantidad_de_anuncios['display']}\tsocial:{cantidad_de_anuncios['social']}."        
        return mensaje
    
    
if __name__ == "__main__":

    video2=Video(100,100,"hola","gato","instream",10)
    social2=Social(10,10,"hola2","chao2","Facebook")
    video3=Video(150,150,"hola","chao3","instream",10)
    display2=Display(120,120,"hola4","chao4","tradicional")
    
    campania1=Campania("Ann",date(2024,1,1),date(2024,3,3),[video2,social2,video3,display2])
    print(campania1)
    campania1.nombre_campania="Karina"
