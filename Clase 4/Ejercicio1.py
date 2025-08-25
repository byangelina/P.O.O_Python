

# par o impar:
# Editar este código para que funcione con una función

# crear una funcion que reciba un argumento com numero entero, el parameto evaluará si es par o impar
# llamar la funcion en el if


"""
contador = 0

numero = int(input("\nIngrese un número: "))

flecha = "-->"

for i in range(1,numero+1):

    if i % 2 == 0 :

        print(i,flecha,"par")

    else:

        print(i,flecha,"impar")

    contador =+ numero

print("\nPrograma finalizado.")
"""



# mi desarrollo



def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
input_numero = int(int(input("\nIngrese un número: ")))

if par_impar(input_numero):
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")




# desarrollado por el profe:
"""def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Ing. número :"))
if es_par(num):
    print("Grabar en base datos")
else:
    print("Enviar correo al usuario que no es par")
"""







