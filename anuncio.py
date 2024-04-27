from abc import ABC, abstractmethod
from error import *


class Anuncio(ABC):
    def __init__(self,ancho,alto,url_archivo,url_click,sub_tipo) -> None:
        super().__init__()
        self.__ancho=ancho
        self.__alto=alto
        self.__url_archivo=url_archivo
        self.__url_click=url_click
        self.__sub_tipo=sub_tipo
        
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self):
        pass
    
    @property
    def url_click(self):
        return self.__url_click
    
    @url_click.setter
    def url_click(self):
        pass
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self.__ancho=ancho if ancho > 0 else 1
        
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,alto):
        self.__alto=alto if alto > 0 else 1
        
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self,sub_tipo):
        self.__sub_tipo=sub_tipo
    
    @classmethod
    def mostrar_formatos(cls):
        print(f"\n{cls.formato}")
        print("---------------------")
        for tipo in cls.subtipos:
            print(tipo)
    
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass
    
    
class Video(Anuncio):
    formato="Video"
    subtipos=("instream","outstream")
    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo,duracion) -> None:
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)
        self.__duracion=duracion
        self.__ancho = 1
        self.__alto = 1
    
    def __str__(self) -> str:
        print(f"{self.formato}")
        print("---------------------")
        for tipo in self.subtipos:
            print(tipo)
        return  super().__str__()
        
    @property
    def sub_tipo(self):
        return self._Anuncio__sub_tipo    
    
    @sub_tipo.setter
    def sub_tipo(self, nuevo_subtipo):
        try:
            if nuevo_subtipo not in self.subtipos:
                raise SubTipoInvalidoError(f"{nuevo_subtipo} No es un valor valido para video.")
            else:
                self._Anuncio__sub_tipo = nuevo_subtipo
        except SubTipoInvalidoError as aviso:
            print(aviso)
            print("\nSubtipos Validos:")
            self.mostrar_formatos()         #agregacion
            print()
            exit()
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho=ancho
        self.__ancho=1
            
        
    
    @property
    def alto(self):
        return self.__alto  
    
    @alto.setter
    def alto(self,alto):
        self.__alto=alto  
        self.__alto=1  
        
    @property
    def duracion(self):
        return self.__duracion    
    
    @duracion.setter
    def duracion(self, nueva_duracion):
        self.__duracion=nueva_duracion if nueva_duracion>0 else 5
        # if  nueva_duracion >0:
        #     self.__duracion=nueva_duracion
        # else:
        #     self.__duracion=5
    
    def comprimir_anuncio(self):
        return "comprension de video no implementada aun"
    
    
    def redimensionar_anuncio(self):
        return "recorte de video no implementado aun"
    
    
    
class Display(Anuncio):
    formato="Display"
    subtipos=("tradicional","native")
    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo) -> None:
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)
        
    def comprimir_anuncio(self):
        return "compresion de anuncios display no implementada aun"
    
    def redimensionar_anuncio(self):
        return "redimensionamiento de anuncios display no implementado aun"
    
    @property
    def sub_tipo(self):
        return self._Anuncio__sub_tipo    
    
    @sub_tipo.setter
    def sub_tipo(self, nuevo_subtipo):
        try:
            if nuevo_subtipo not in self.subtipos:
                raise SubTipoInvalidoError(f"\n\n{nuevo_subtipo} No es un valor valido para Display.")
            else:
                self._Anuncio__sub_tipo = nuevo_subtipo
        except SubTipoInvalidoError as aviso:
            print(aviso)
            print("\nSubtipos Validos:")
            self.mostrar_formatos()         #agregacion
    
    
class Social(Anuncio):
    formato="Social"   
    subtipos=("Facebook","Linkedin")
    def __init__(self, ancho, alto, url_archivo, url_click, sub_tipo) -> None:
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)
        
    def comprimir_anuncio(self):
        return "compresion de anuncios de redes sociales no implementada aun"
    
    def redimensionar_anuncio(self):
        return "redimensionamiento de anuncios de redes sociales no implementado aun"

    @property
    def sub_tipo(self):
        return self._Anuncio__sub_tipo    
    
    @sub_tipo.setter
    def sub_tipo(self, nuevo_subtipo):
        try:
            if nuevo_subtipo not in self.subtipos:
                raise SubTipoInvalidoError(f"\n\n{nuevo_subtipo} No es un valor valido para Social.")
            else:
                self._Anuncio__sub_tipo = nuevo_subtipo
        except SubTipoInvalidoError as aviso:
            print(aviso)
            print("\nSubtipos Validos:")
            self.mostrar_formatos()         #agregacion

# video1=Video(100,100,"hola","chao","hola",1)
# video1.sub_tipo="chao"


if __name__ =="__main__":
    
    # print(video1.alto,video1.ancho, video1.duracion,video1.sub_tipo)
    # video1.alto=10
    # video1.ancho=50
    # video1.duracion=0
    # print(video1.alto,video1.ancho, video1.duracion,video1.sub_tipo)
    # print(video1.comprimir_anuncio())
    # print(video1.redimensionar_anuncio())
    # print(video1)
    display1=Display(100,100,"hola","chao","instream")
    display1.sub_tipo="chao"
    display1.sub_tipo="tradicional"
    print(display1.sub_tipo)
    # print(display1.comprimir_anuncio())
    # print(display1.redimensionar_anuncio())
    social1=Social(100,100,"hola","chao","instream")
    social1.sub_tipo="hola"
    social1.sub_tipo="Facebook"
    print(social1.sub_tipo)
    # print(social1.comprimir_anuncio())
    # print(social1.redimensionar_anuncio())
    # print(video1.mostrar_formatos(), display1.mostrar_formatos(),social1.mostrar_formatos())