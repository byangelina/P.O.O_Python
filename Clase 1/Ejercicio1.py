"""
Desarrolle un programa que permita ingresar 10 numeros y despliegue el mayor.

Restriccion: no puede usar listas, funcion max, no chatgpt.
"""

num = 0

for i in range (1,11):
    numero_ingresado = int(input("Ingrese un número: "))   
    if num >= numero_ingresado:
        num += 1
        break

print(f"el número mayor es: {i} ")

