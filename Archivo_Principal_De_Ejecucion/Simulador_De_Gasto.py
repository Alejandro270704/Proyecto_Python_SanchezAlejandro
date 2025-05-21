#importar arhivo json


#se importa la carpeta donde tiene el archivo de funciones para la ejecucion

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Archivos_modulos import Funciones
resultado,datos,usuarioActual=Funciones.menusesion()
if resultado:
    Funciones.simuladorGasto(datos, usuarioActual)
else:
    print("No se pudo iniciar sesión. Cerrando programa.")

