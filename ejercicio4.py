"""
Desarrolle un programa que permita ingresar 3 numeros y desplegar el mayor

- sin ciclos, sin listas...
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


