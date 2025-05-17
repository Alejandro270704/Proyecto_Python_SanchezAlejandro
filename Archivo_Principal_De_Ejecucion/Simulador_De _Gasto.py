#importar modulo 
import json 
#inicio de sesion 
listaJSON={}
print         ("    inicio de sesión          ")
iniciar=int (input(" 1.iniciar sesión")),
crear= int(input  (" 2.crear usuario   "))
opc=int (input("eliga una opción numerica :"))
if opc ==1:
    inicioDeSesion=input("ingresa tu nombre :")
    clavedeUsuario=input("ingresa la clave :")
elif opc ==2 :
    nombre=input ("escriba su nombre completo:")
    clave=input("escriba una clave :")
    print ("usuario creado ")
    

if opc== 1 and 2 :
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
            print ()
