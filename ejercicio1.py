
# ejemplo funciones
"""def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma es: {resultado}")"""


# ejemplo funciones
"""def saludar():
    print("¡Hola! Espero que tengas un gran día.")

saludar()"""



# función con un parámetro
"""def holaConNombre(name):
  print("Hello " + name + "!")

holaConNombre("Ada")"""  # llamada a la función, 'Hello Ada!' se muestra en la consola



# Variables Locales: Son aquellas que se declaran dentro de una función y solo pueden ser accedidas dentro de esa función.
"""def mi_funcion():
    x = 10  # Variable local
    print(x)"""



# Variables Globales: Son aquellas que se declaran fuera de cualquier función y pueden ser accedidas desde cualquier parte del programa.
"""y = 20  # Variable global
def otra_funcion():
    print(y)  # Accede a la variable global"""


# par o impar



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

# crear una funcion que reciba un argumento com numero entero, el parameto evaluará si es par o impar
# llamar la funcion en el if


# mi desarrollo (funciona pero esta mal)
input_numero = int(int(input("\nIngrese un número: ")))

def es_par(input_numero):
    return None

def es_impar(input_numero):
    return None

if input_numero % 2 == 0 :
    print(es_par)
else:
    print(es_impar)



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






































