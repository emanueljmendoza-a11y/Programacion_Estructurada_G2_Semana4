# Programa para una ferretería

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal):
    descuento = 0

    if subtotal >= 3000:
        descuento = subtotal * 0.08

    return descuento


def calcular_iva(subtotal, descuento):
    subtotal_descuento = subtotal - descuento
    iva = subtotal_descuento * 0.15
    return iva


def mostrar_compra(producto, subtotal, descuento, iva):
    total = subtotal - descuento + iva

    print("\n----- RESUMEN DE LA COMPRA -----")
    print("Producto:", producto)
    print("Subtotal: C$", subtotal)
    print("Descuento: C$", descuento)
    print("IVA (15%): C$", iva)
    print("Total: C$", total)


# Entrada de datos
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: C$ "))
cantidad = int(input("Ingrese la cantidad: "))

# Cálculos
subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal)
iva = calcular_iva(subtotal, descuento)

# Mostrar resultados
mostrar_compra(producto, subtotal, descuento, iva)