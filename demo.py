from campania import *
from datetime import date, datetime
import os


os.system("cls") if os.name == "nt" else os.system("clear")
anuncio_video=Video(100,100,"hola","chao","instream",15)
nueva_campania=Campania("Campaña del terror",date(2024,1,1),date(2024,4,11),[anuncio_video])
print(nueva_campania)

try:
    nuevo_nombre_campania=input("ingrese un nuevo nombre de campaña: ")
    nuevo_subtipo_anuncio=input("ingrese nuevo subtipo para anuncio: ")
    nueva_campania.nombre_campania=nuevo_nombre_campania
    nueva_campania.anuncios[0].sub_tipo=nuevo_subtipo_anuncio
    print(f"\nNUEVA CAMPAÑA: \n\n")
    print(nueva_campania)
except:
    pass
