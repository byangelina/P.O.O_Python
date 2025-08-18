"""
Desarrolle un programa que permita ingresar 3 numeros
y desplegar el mayor

- sin ciclos, sin listas...
"""

"""num1 = int(input("\nIngrese el primer número: "))

num2 = int(input("\nIngrese el segundo número: "))

num3 = int(input("\nIngrese el tercer número: "))

n1 = num1 > num2 and num3 
n2 = num2  > num1 and num3
n3 = num3 > num2 and num1

n_mayor = (n1 or n2 or n3)

print(f"\nEl número mayor es: {n_mayor}")

print("Programa finalizado.")
"""


n1 = int(input("\nIngrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))


if n1 > n2 and n1 > n3:
    print(f"\nEl número mayor es: {n1}") 

elif n2 > n3:
    print(f"\nEl número mayor es: {n2}") 

else:
    print(f"\nEl número mayor es: {n3}") 

print("\nPrograma finalizado.")


