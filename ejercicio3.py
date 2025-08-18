# par o impar


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








