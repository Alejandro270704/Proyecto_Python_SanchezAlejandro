#importar el archivo json para leer guardar y enviar informacion 
import json 
#importo libreria de captura de tiempo 

from datetime import datetime
from tabulate import tabulate
# se crea una funcion para crear un usuario
def crear_usuario(datos):
    
    boleano=True
    while boleano :
        nombre=input ("escriba su nombre completo:")
        for q in datos :
            if q["usuario"]==nombre:
                print (" el usuario ya esta registrado ")
                print ("digite otro nombre")
                break 
        else :
            boleano= False 
        
    clave=input("escriba una contraseña :")
    
    usuarioActual={"usuario":nombre,"clave":clave,"gastos":[]}
    datos.append(usuarioActual)
    with open("Archivo_JSON/Datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
            
    print ("usuario creado ")
    return datos,usuarioActual
#se crea una funcion para iniciar sesion por si el usuario ya tiene una cuenta
def iniciosesion(datos):
    repetidor=True
    while repetidor:
        inicioDeSesion=input("ingresa tu nombre :")
        clavedeUsuario=input("ingresa la clave :")
        
        for login in datos:
            if login["usuario"]==inicioDeSesion and login["clave"]==clavedeUsuario:
                print ("inicio sesión correctamente")
                usuarioActual =login 
                repetidor=False
                break 
            
            
            
        else :
            print("Usuario o clave incorrecta")
            print ("quieres crear un usuario?")
            eleccion=int (input("1:si , 2:no :"))
            if eleccion==1 :
                datos = crear_usuario(datos)
                return datos,usuarioActual
    return datos,usuarioActual
        
#  opcional : se crea una funcion para el menu de sesion 
def menusesion():
    

    with open("Archivo_JSON/Datos.json", "r") as archivo:
        datos = json.load(archivo)
    print("    inicio de sesión          ")
    print(" 1.iniciar sesión")
    print(" 2.crear usuario   ")
    opc=int(input("eliga una opción numerica :"))
    
    #dentro de la funcion se invocan a las dos funciones anteriores para que funcione el programa (crear usuario,iniciar sesion)
    if opc ==1:
        datos,usuarioActual=iniciosesion(datos)
    
        
    elif opc ==2 :
        datos,usuarioActual=crear_usuario(datos)
    

    return True ,datos,usuarioActual

def nuevoGasto(datos,usuarioActual):
    
    for usuario in datos:
        if usuario["usuario"] == usuarioActual["usuario"]:
            print ("menu de gastos")
            monto=float(input("digite su gasto:"))
            fechaActual=datetime.now().strftime("%d/%m/%y %H:%M")
            print (fechaActual)
            print("categoria")
            categoria=input("digita la categoria:")
            opinion=int(input("quieres agregar una descripcion?:1:si  2:no:"))
            if opinion==1 :
                descripcion=input("escribe la descripcion")
            else:
                descripcion=str()
            usuarioActual["gastos"].append({"monto":monto, "categoria":categoria, "descripcion":descripcion})
            print("")
            
            
            with open("Archivo_JSON/Datos.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
    return  datos,usuarioActual

def lista_gasto(datos,usuarioActual):
    print ("lista de gastos")
    print("1.ver todos los datos ")
    print("2.filtrar por fecha/categoria")
    opc_lista=int(input("elige opcion numerica:"))
    if opc_lista==1:
        for usuario in datos:
            if usuario["usuario"] == usuarioActual["usuario"]:
                print(tabulate(usuarioActual["gastos"]))
    elif opc_lista==2:
        print ("listar gasto por:")
        print ("1.fecha")
        print ("2.categoria")
        opc=int(input("eliga opcion numerica:"))
        if opc ==1:
            repetidor=True
            while repetidor:
                try:
                    fecha=datetime(input("digite la fecha (formato dd/mm/yyyy):")).strftime("%d/%m/%y")
                    print(f"ingresaste la fecha {fecha}")
                    repetidor=False  
                except TypeError:
                    print("formato de fecha invalido")





