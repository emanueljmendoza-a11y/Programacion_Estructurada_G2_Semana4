import crud

def leerdatos():
    edad = int(input("Ingrese la edad: "))
    crud.agregar(edad) 

def menu():
    print("1. Agregar edad")
    print("2. Mostrar edades")
    print("3. Calcular edad más alta y más baja")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


def main():
    while True:
        opcion = menu()
        if opcion == 1:
            leerdatos()
        elif opcion == 2:
            crud.mostrar()
        elif opcion == 3:
            crud.calcular_edad_mas_alta_y_mas_baja()
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()