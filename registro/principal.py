import crud
def leerdatos ():
  print("Dime tu nota:")
  nota = int(input())
  crud.agregar(nota)


def menu ():
    print("""
    1. Ingresar notas
    2. Mostrar notas
    3. Evaluar notas
    0. Salir
    Digita una opcion valida:

    """ )
    opcion = int(input())
    return opcion


    import crud
def main():
    while True:
        op = menu()
        if op == 1:
            leerdatos()
            
        elif op == 2:
            print(crud.mostrar())

        elif op == 3:
            #Esperando
            print("En construccion")
        elif op == 0:
            print("Adios")
            break
        else:
            print("opcion invalida...")



main()
    