#importar el archivo json para leer guardar y enviar informacion 
import json 
import os
#defino una funcion para limpiar la pantalla 
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
#importo libreria de captura de tiempo 

from datetime import datetime
#importo liberia de tablas
from tabulate import tabulate
# se crea una funcion para crear un usuario
def crear_usuario(datos):
    limpiar_pantalla()
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
    
    usuarioActual={"usuario":nombre,"clave":clave,"gastos":[],"reporte":[]}
    datos.append(usuarioActual)
    with open("Archivo_JSON/Datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
            
    print ("usuario creado ")
    input("presiona enter para continuar")
    limpiar_pantalla()
    return datos,usuarioActual
#se crea una funcion para iniciar sesion por si el usuario ya tiene una cuenta
def iniciosesion(datos):
    limpiar_pantalla()
    repetidor=True
    while repetidor:
        inicioDeSesion=input("ingresa tu nombre :")
        clavedeUsuario=input("ingresa la clave :")
        
        for login in datos:
            if login["usuario"]==inicioDeSesion and login["clave"]==clavedeUsuario:
                print ("inicio sesión correctamente")

                usuarioActual =login 
                repetidor=False
                input("presiona enter para continuar")
                limpiar_pantalla()
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
    
    limpiar_pantalla()
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
#defino una funcion para entrar un gasto nuevo 
def nuevoGasto(datos,usuarioActual):
    limpiar_pantalla()
    
    for usuario in datos:
        if usuario["usuario"] == usuarioActual["usuario"]:
            print ("menu de gastos")
            monto=float(input("digite su gasto:"))
            fechaActual=datetime.now().strftime("%d/%m/%Y")
            print("categoria")
            categoria=input("digita la categoria:")
            opinion=int(input("quieres agregar una descripcion?:1:si  2:no:"))
            if opinion==1 :
                descripcion=input("escribe la descripcion")
                
            else:
                descripcion=str()
                print ("no se agrego ninguna descripcion")
            print ("se añadio el gasto")
            usuarioActual["gastos"].append({"monto":monto, "categoria":categoria, "descripcion":descripcion,"fecha":fechaActual})
            
            
            
            with open("Archivo_JSON/Datos.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
    return  datos,usuarioActual
#defino la opcion para listar todos los gastos o listar por categoria y fechas
def lista_gasto(usuarioActual):
    limpiar_pantalla()
    print ("lista de gastos")
    print("1.ver todos los datos ")
    print("2.filtrar por fecha/categoria")
    opc_lista=int(input("elige opcion numerica:"))
    if opc_lista==1:
                print(tabulate(usuarioActual["gastos"], headers="keys"))
    elif opc_lista==2:
        print ("listar gasto por:")
        print ("1.fecha")
        print ("2.categoria")
        opc=int(input("eliga opcion numerica:"))
        if opc ==1:
            repetidor=True
            while repetidor:
                try:
                    fecha = datetime.strptime(input("digite la fecha (formato dd/mm/yyyy):"), "%d/%m/%Y").strftime("%d/%m/%Y")
                    print(f"ingresaste la fecha {fecha}")
                    gastosfiltro=[gasto for gasto in usuarioActual["gastos"]
                    if gasto["fecha"]==fecha ]
                    
                    repetidor=False  
                    if gastosfiltro:
                        print(tabulate(gastosfiltro, headers="keys"))
                    else :
                        print ("no hay gastos para esa fecha")
                except ValueError:
                    print("formato de fecha invalido")
        elif opc ==2 :
            repetidor=True
            while repetidor:
                print ("filtrar por categoria")
                buscadorCategoria=input("escriba la categoria a buscar")
                gastosfiltro = [
                gasto for gasto in usuarioActual["gastos"]
                if gasto["categoria"].lower() == buscadorCategoria.lower() ]

                if gastosfiltro:
                    print(tabulate(gastosfiltro, headers="keys"))
                    repetidor = False
                else:
                    print("No se encontró la categoría.")
                    print("")
                    print("¿Digitar otra vez categoría o volver al menú?")
                    salirmenu = int(input("1: Filtrar categoría   2: Salir a menú: "))
                    if salirmenu == 2:
                        repetidor = False
#se crea una funcionn para calcular gasto diario 
def calcular_Diario (usuarioActual,diccionarioCategoria,total):
            print ("formato esperado : dd/mm/yyyy")
            fechaInicio=(input("digite la fecha exacta para calcular total de gasto :"))
            fechaInicio=datetime.strptime(fechaInicio,"%d/%m/%Y") 
            for gasto in usuarioActual["gastos"]:
                if gasto["fecha"]==fechaInicio.strftime("%d/%m/%Y"):
                    categoriaN=gasto["categoria"]
                    
                    if categoriaN in diccionarioCategoria:
                        
                        diccionarioCategoria[categoriaN]+=gasto["monto"]
                    else :
                        diccionarioCategoria[categoriaN]=gasto["monto"]
                    total+=gasto["monto"]
            for categoria,monto in sorted(diccionarioCategoria.items(), key=lambda x: x[1], reverse=True):
                print (categoria,":",monto)
            print(f"Total de gastos: {total}")
#se crea una funcionn para calcular gasto semanal
def calcular_semanal (usuarioActual,diccionarioCategoria,total):
    print ("formato esperado : dd/mm/yyyy")
    fechaInicio=(input("digita un dia de la semana a consultar "))
    fechaInicio=datetime.strptime(fechaInicio,"%d/%m/%Y")
    semanaUsuario = fechaInicio.isocalendar()[1]
    gastoUsuario = fechaInicio.year   
    for gastos in usuarioActual["gastos"]:
                
                gastoSemana=datetime.strptime(gastos["fecha"],"%d/%m/%Y")
                categoriaN=gastos["categoria"]
            
                semana=gastoSemana.isocalendar()[1]
                Gasto = gastoSemana.year
            
                
                if semana== semanaUsuario and Gasto == gastoUsuario:
                    
                    if categoriaN in diccionarioCategoria:
                        
                        diccionarioCategoria[categoriaN]+=gastos["monto"]
                    else :
                        diccionarioCategoria[categoriaN]=gastos["monto"]
                    total +=gastos["monto"]  
    for categoria,monto in sorted(diccionarioCategoria.items(), key=lambda x: x[1], reverse=True):
        print (categoria,":",monto)
    print(f"Total de gastos: {total}")
#se crea una funcionn para calcular gasto mensual
def calcular_mes (usuarioActual,diccionarioCategoria,total):
            print ("formato esperado:mm/yyyy  ")
            fechaInicio=(input("digite el mes y año : "))
            fechaInicio=datetime.strptime(fechaInicio,"%m/%Y")
            fechaMes=fechaInicio.month
            fechaN=fechaInicio.year
            for gastos in usuarioActual["gastos"]:
                gastomes=datetime.strptime(gastos["fecha"],"%d/%m/%Y")
                categoriaN=gastos["categoria"]
                
                
                mes=gastomes.month
                anio=gastomes.year
                if fechaMes==mes and fechaN==anio:
                    total+=gastos["monto"]
                    if categoriaN in diccionarioCategoria:
                        
                        diccionarioCategoria[categoriaN]+=gastos["monto"]
                    else :
                        diccionarioCategoria[categoriaN]=gastos["monto"]
                
            for categoria,monto in sorted(diccionarioCategoria.items(), key=lambda x: x[1], reverse=True):
                print (categoria,":",monto)
            print(f"Total de gastos: {total}")

#funcion para calcular gastos diarios,semanales ,mensuales 
def calcularGasto(usuarioActual):
    
    limpiar_pantalla()
    total=0
    diccionarioCategoria={}
    print("calcular total de gastos")
    print (" escoja el filtro para calcular el total")
    print("1.diario")
    print("2.semanal")
    print("3.mensual")
    opcion=int(input("opcion numerica :"))
    try :
        if opcion==1:
            calcular_Diario(usuarioActual,diccionarioCategoria,total)
            
            
            
        elif opcion==2:
            
            calcular_semanal(usuarioActual,diccionarioCategoria,total)
        elif opcion==3:
            calcular_mes(usuarioActual,diccionarioCategoria,total)

            
    except ValueError:
        print ("formato invalido")
    input("Presione Enter para volver al menú...")
def verYguardar_reporte(fechaInicio,diccionarioCategoria,total):
    reporte = {
        "fecha": fechaInicio.strftime("%d/%m/%Y"),
        "categorias": diccionarioCategoria,
        "total": total}
    print ("=====================================")
    print (f"reporte diario para {fechaInicio.strftime('%d/%m/%Y')}")
    print ("=====================================")
    for categoria,monto in sorted(diccionarioCategoria.items(), key=lambda x: x[1], reverse=True):
            print (categoria,":",monto)
            print("=============================================")
            print (f"         Total de gastos: {total}")
            input("presione cualquier tecla para continuar ")
    
    
    return reporte


#creo una funcion para generar reporte 
def generarReporte(usuarioActual,datos):
    limpiar_pantalla()
    
    print("=============================================")
    print("           Generar Reporte de Gastos         ")
    print("=============================================")
    print("      1. Diario")
    print("      2. Semanal")
    print("      3. Mensual")
    print("      4. Regresar al menú principal")
    print("=============================================")
    opc=int (input("digite opcion numerica:"))
    total=0
    diccionarioCategoria={}
    
    if opc ==1:
        print ("formato esperado : dd/mm/yyyy")
        fechaInicio=(input("digite la fecha exacta para calcular total de gasto :"))
        fechaInicio=datetime.strptime(fechaInicio,"%d/%m/%Y") 
        for gasto in usuarioActual["gastos"]:
                if gasto["fecha"]==fechaInicio.strftime("%d/%m/%Y"):
                    categoriaN=gasto["categoria"]
                    
                    if categoriaN in diccionarioCategoria:
                        
                        diccionarioCategoria[categoriaN]+=gasto["monto"]
                    else :
                        diccionarioCategoria[categoriaN]=gasto["monto"]
                    total+=gasto["monto"]
        print("=============================================")
        print ("             ¿Que desea hacer?")
        print("=============================================")
        print ("               1.ver reporte")
        print ("               2.guardar reporte")
        print("=============================================")
        opcion=int(input(" digite opcion numerica:"))
        if opcion==1:
            reporte=verYguardar_reporte(fechaInicio,diccionarioCategoria,total)


        elif opcion==2:
            if "reporte" not in usuarioActual:
                usuarioActual["reporte"] = []
            reporte = verYguardar_reporte(fechaInicio, diccionarioCategoria, total)
            usuarioActual["reporte"].append(reporte)
            
            
            with open("Archivo_JSON/Datos.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
            print(f"se guardó correctamente el reporte: {reporte}")
    elif opc==2:
        print ("formato esperado : dd/mm/yyyy")
        fechaInicio=(input("digita un dia de la semana a consultar "))
        fechaInicio=datetime.strptime(fechaInicio,"%d/%m/%Y")
        semanaUsuario = fechaInicio.isocalendar()[1]
        gastoUsuario = fechaInicio.year   
        for gastos in usuarioActual["gastos"]:
            
            gastoSemana=datetime.strptime(gastos["fecha"],"%d/%m/%Y")
            categoriaN=gastos["categoria"]
            
            semana=gastoSemana.isocalendar()[1]
            Gasto = gastoSemana.year
            
                
            if semana== semanaUsuario and Gasto == gastoUsuario:
                    
                if categoriaN in diccionarioCategoria:
                        
                    diccionarioCategoria[categoriaN]+=gastos["monto"]
                else :
                    diccionarioCategoria[categoriaN]=gastos["monto"]
                total +=gastos["monto"]  
        print("=============================================")
        print ("             ¿Que desea hacer?")
        print("=============================================")
        print ("               1.ver reporte")
        print ("               2.guardar reporte")
        print("=============================================")
        opcion=int(input(" digite opcion numerica:"))
        if opcion==1:
            reporte=verYguardar_reporte(fechaInicio,diccionarioCategoria,total)
        elif opcion==2:
            reporte=verYguardar_reporte(fechaInicio,diccionarioCategoria,total)
            usuarioActual["reporte"].append(reporte)
            
        
    elif opc==3:
        
        print ("formato esperado:mm/yyyy  ")
        fechaInicio=(input("digite el mes y año : "))
        fechaInicio=datetime.strptime(fechaInicio,"%m/%Y")
        fechaMes=fechaInicio.month
        fechaN=fechaInicio.year
        for gastos in usuarioActual["gastos"]:
                gastomes=datetime.strptime(gastos["fecha"],"%d/%m/%Y")
                categoriaN=gastos["categoria"]
                
                
                mes=gastomes.month
                anio=gastomes.year
                if fechaMes==mes and fechaN==anio:
                    
                    if categoriaN in diccionarioCategoria:
                        
                        diccionarioCategoria[categoriaN]+=gastos["monto"]
                    else :
                        diccionarioCategoria[categoriaN]=gastos["monto"]
                total+=gastos["monto"]
        print("=============================================")
        print ("             ¿Que desea hacer?")
        print("=============================================")
        print ("               1.ver reporte")
        print ("               2.guardar reporte")
        print("=============================================")
        opcion=int(input(" digite opcion numerica:"))
        if opcion==1:
            reporte=verYguardar_reporte(fechaInicio,diccionarioCategoria,total)
            
        elif opcion==2:
            reporte=verYguardar_reporte(fechaInicio,diccionarioCategoria,total)
            usuarioActual["reporte"].append(reporte)
    elif opc==4:
        print("salio del reporte")
    else :
        print("opcion no valida")


#creo una funcion para el menu del simluadorde gasto 
def simuladorGasto (datos,usuarioActual):
    
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
            datos,usuarioActual=nuevoGasto(datos,usuarioActual)
        elif opcion==2 :
            lista_gasto(usuarioActual)
        elif opcion==3 :
            calcularGasto(usuarioActual)
        elif opcion==4 :
            generarReporte(usuarioActual,datos)
        elif opcion==5 :
            boleano=False
            print ("ha salido del programa ")
            
        else :
            print ("opcion no valida")