#Arriendo de vivienda
import Libreria as lb
while True:
    print("1.Registrar usuario ")
    print("2.Viviendas disponibles")
    print("3.Arriendo de viviendas")
    print("4.Salir")
    opcion=int(input("Elige una opcion:"))
    
    if opcion==1:
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
     dia=int(input("Ingrese el dia en el que nacio:"))
     if 1 <= dia <= 31:
        break
     else:
      print("¡Ingrese un dia valido!")
    while True:    
     mes=int(input("Ingrese el mes en el que nacio:"))
     if 1 <= mes <= 12:
         break
     else:
         print("¡Ingrese un mes valido!")
    while True:
     año=int(input("Ingrese el año en el que nacio:"))
     if 1960 <= año <= 2003:
         break
     else:
         print("¡Ingrese una año valido!(Si nacio antes del año 1960 y despues del año 2003 no sera aceptado)")
    print("Su fecha de nacimiento es:",dia,mes,año)
    
