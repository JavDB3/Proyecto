#Arriendo de vivienda
import libreria as lb
while True:
    usuario=input("Ingrese el usuario:")
    usuario_correcto="colocolo"
    if usuario==usuario_correcto:
        break
    else:
        print("Ingrese un usuario correcto")


intentos_disponibles = 3
contraseña_correcta = "1991"

while intentos_disponibles > 0:
    contraseña = input("Ingrese la contraseña: ")
    
    if contraseña == contraseña_correcta:
        print("¡Has sido registrado!")
        break
    else:
        intentos_disponibles-=1
        if intentos_disponibles > 0:
            print("Ingresaste una contraseña incorrecta,Recuerda que solo tienes tres intentos.")
        else:
            print("Has gastado todos los intentos,Seras expulsado del programa.")
        

def main():
    while True:
        print("1. Registrar usuario")
        print("2. Viviendas disponibles")
        print("3. Arriendo de viviendas")
        print("4. Salir")
        
        try:
            opcion = int(input("Eliga una opcion: "))
        except ValueError:
            print("¡Por favor, ingrese un número válido!")
            continue
        
        if opcion == 1:
            lb.registrar_usuario()
        elif opcion == 2:
            lb.viviendas_disponibles()
        elif opcion == 3:
            lb.arriendo_viviendas()
        elif opcion == 4:
            print("Ha salido del programa")
            break
        else:
            print("¡Opción no válida! elija una opción del 1 al 4.")


main()
    
