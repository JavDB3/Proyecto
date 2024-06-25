def registrar_usuario():
    while True:
        nomb = input("Ingrese su primer nombre y su primer apellido: ")
        nombre_apellido = nomb.split()
        
        if len(nombre_apellido) == 2:
            break  
        else:
            print("¡Ingrese solamente su primer nombre y su primer apellido!")  

    print("Nombre y apellido ingresados:", nomb)  
    print("[Ingrese su fecha de nacimiento]")
    
    while True:
        dia = int(input("Ingrese el dia en el que nacio: "))
        if 1 <= dia <= 31:
            break
        else:
            print("¡Ingrese un dia valido!")
    
    while True:
        mes = int(input("Ingrese el mes en el que nacio: "))
        if 1 <= mes <= 12:
            break
        else:
            print("¡Ingrese un mes valido!")
    
    while True:
        año = int(input("Ingrese el año en el que nacio: "))
        if 1960 <= año <= 2003:
            break
        else:
            print("¡Ingrese una año valido! (Si nacio antes del año 1960 y despues del año 2003 no sera aceptado)")
    
    print("Su fecha de nacimiento es:", dia, "/", mes, "/", año)
    fecha_nacimiento=dia,mes,año

def viviendas_disponibles():
    while True:
        print("1. Regiones disponibles")
        print("2. comunas disponibles")
        print("3. viviendas disponibles")
        print("4. Salir")
        opcion=int(input("Elige una opcion:"))
        if opcion==1:
            print("En este momento solo se encuentran disponibles la region metropolitana y la region del bio bio")
        if opcion==2:
            print("Las comunas disponibles son en la region metropolitana:Colina y las condes y en la region del bio bio:Talcahuano y concepcion")
        if opcion==3:
            print("Las viviendas disponibles  son las siguientes")
            print(casa_colina)
            print(casa_condes)
            print(casa_talcahuano)
            print(casa_concepcion)
        if opcion==4:
            print("Has elejido salir")
            break
        else:
            print("Elije una opcion correcta")
            
        
            

casa_colina="""En colina se encuentra una  casa de:
-2 pisos
-tres dormitorios
-un baño ademas
-un living
-un comedor
- una cocina
- un amplio estacionamiento para 2 o 3 vehículos"""

casa_condes="""En las condes se encuentra un departamento que cuenta con:
-125 metros cuadrados
-una terreza de 15 metros cuadrados
- de cuatro dormitorios
-tres baños
-una bodega
-dos estacionamientos"""

casa_talcahuano="""En talcahuano se encuentra disponible un departamento de:
-57 metros cuadrados
-Dos baños
-Se admiten mascotas
- Dos estacionamientos
-construido en el año: 2021
- Una bodega"""

casa_concepcion="""En concepcion se encuentra una casa de:
- 160 metros cuadrados utiles y superficie total de 220 metros cuadrados totales
- seis dormitorios
- cinco baños
- No Admite mascotas
- dos estacionamientos
-Cocina
- Bodega"""


