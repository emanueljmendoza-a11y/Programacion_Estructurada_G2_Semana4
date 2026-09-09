"""Crear un módulo para guardar edades de un 
estudiante y decir que si son niños , joven , adultos y adultos mayores
y calcular edad mas alta y edad mas baja de los estudiantes"""


edades = []

def agregar(edad):
    edades.append(edad)
    print(f"Edad {edad} agregada correctamente.")

def clasificar_edad(edad):
    if edad <= 13:
        return "Niño(Segui jugando minecraft como jeremy)"
    elif edad < 18:
        return "Joven(tas chavalo)"
    elif edad < 60:
        return "Adulto.. Ya tenes tu casa?"
    else:
        return "Ya ta viejo , no se ha jubilado?"

def mostrar():
    if not edades:
        print("No hay edades registradas.")
        return
    
    print("\n Lista de edades ")
    for i, edad in enumerate(edades, 1):
        categoria = clasificar_edad(edad)
        print(f"{i}. {edad} años - {categoria}")

def calcular_edad_mas_alta_y_mas_baja():
    if not edades:
        print("No hay edades para calcular.")
        return
    
    max_edad = max(edades)
    min_edad = min(edades)
    
    print(f"\nEdad más alta: {max_edad} años ({clasificar_edad(max_edad)})")
    print(f"\nEdad más baja: {min_edad} años ({clasificar_edad(min_edad)})")