def calcular_total():
    total = 5000
    print("El total dentro de la función es:", total)
    return total

total = calcular_total()

print("El total fuera de la función es:", total)
#Aquí calcular_total() devuelve total con return, y afuera se guarda en una variable (también llamada total,  pero es una variable distinta, del ámbito global) que sí puede usarse en el segundo print.