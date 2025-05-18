import json 
def inicioSesion():
    with open('Archivo_JSON/Datos.json', 'r') as archivo:
     datos= json.load(archivo)
    print         ("    inicio de sesión          ")
    print             (" 1.iniciar sesión")
    print             (" 2.crear usuario   ")
    opc=int(input("eliga una opción numerica :"))
    
   
    
    if opc ==1:
        repetidor=True
        while repetidor:
            inicioDeSesion=input("ingresa tu nombre :")
            clavedeUsuario=input("ingresa la clave :")
            
            for login in datos:
                if login["usuario"]==inicioDeSesion:
                    if login["contraseña"]==clavedeUsuario:
                        
                        print ("inicio sesión correctamente")
                        repetidor=False
                        break 
                else:
                    print("Usuario o clave incorrecta")
                    break
                    
                    
            else :
                print ("usuario o clave incorrecta")
                print (input ("quieres crear un usuario?"))
                eleccion=int (input("1:si , 2:no :"))
                if eleccion ==1 :
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
    
                    datos.append({"usuario":nombre,"contraseña":clave})
                    with open("Archivo_JSON/Datos.json", "w") as archivo:
                     json.dump(datos, archivo, indent=4)
             
                    print ("usuario creado ")
                    
            
                    
    elif opc ==2 :
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
    
        datos.append({"usuario":nombre,"contraseña":clave})
        with open("Archivo_JSON/Datos.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
             
        print ("usuario creado ")
        