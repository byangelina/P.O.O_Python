

# código del cliente:


"""
detergente = 300
suavizante = 100

while True:
    try:
        n=int(input("Ingrese la cantidad de kilos de ropa a lavar: "))
        detergente_total = (n * detergente)
        suavizante_total = (n * suavizante)
        print("Para lavar",n,"Kilos de ropa se necesita", detergente_total," gramos de detergente y",suavizante_total,"gramos de suavizante")
        break
    except ValueError:
        print("Ingrese un número entero válido")
"""

# versión mejorada del código:
# el cliente no sabe de gramos
# 1000 gramos son un kilo
# en ves de decir "necesitas 1000 gramos", decir "necesitas 1 kilo de..." o "1,2 kilos...", etc.


gramos = 1000

kilo = 1 * gramos

cantidad_k = ("Ingrese candidad de kilos")

d = 300

s = 100



"""Detergente = 300
suavizante = 100

while True:
    try:
        n=int(input("Ingrese la cantidad de kilos de ropa a lavar: "))
        detergente_total = (n * detergente)
        suavizante_total = (n * suavizante)
        print("Para lavar",n,"Kilos de ropa se necesita", detergente_total," gramos de detergente y",suavizante_total,"gramos de suavizante")
        break
    except ValueError:
        print("Ingrese un número entero válido")
"""