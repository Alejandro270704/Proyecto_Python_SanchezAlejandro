#importar arhivo json


#se importa la carpeta donde tiene el archivo de funciones para la ejecucion

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Archivos_modulos import Funciones
resultado,datos,usuarioActual=Funciones.menusesion()




if resultado==True:
    
    boleano=True
    while boleano :

        #simulador de gasto 

        print ("=============================================")
        print ("        Simulador de Gasto Diario            ")
        print ("=============================================")
        print ("          Seleccione una opción:             ")
        print ("         1. Registrar nuevo gasto            ")
        print ("         2. Listar gastos                  ")
        print ("         3. Calcular total de gastos")
        print ("         4. Generar reporte de gastos")
        print ("         5. Salir")
        print ("=============================================")
        opcion=int(input("eliga una opción numerica :"))
        if opcion==1 :
            datos,usuarioActual=Funciones.nuevoGasto(datos,usuarioActual)
        elif opcion==2 :
            
            Funciones.lista_gasto(datos,usuarioActual)
        elif opcion==3 :
            print ()
        elif opcion==4 :
            print ()
        elif opcion==5 :
            boleano=False
            print ("ha salido del programa ")
            
        else :
            print ("opcion no valida")