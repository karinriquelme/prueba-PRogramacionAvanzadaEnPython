from  datetime import datetime



class Errores(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.mensaje_error=args[0]
        
    def crear_log(self, mensaje_error):  
        linea_error=datetime.now().strftime("%d-%m-%Y %H:%M:%S")+f" -- {mensaje_error}.\n"
        with open("error.log","a+",encoding="utf-8") as archivo:
            archivo.write(linea_error)
        

class SubTipoInvalidoError(Errores):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.crear_log(self.mensaje_error)


class LargoExcedidoError(Errores):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.crear_log(self.mensaje_error)