contador = 0

def aumentar_contador():
    global contador
    contador = contador + 1

print("Antes:", contador)

aumentar_contador()
aumentar_contador()
aumentar_contador()

print("Después:", contador)