# Punto 300.0

numero_casos = int(input())

for i in range(numero_casos):
    num = str(input())
    indice = -1
    iguales = 0
    for x in range(0,int(len(num)/2)):
        if num[x] == num[indice]:
            iguales=iguales+1
        indice=indice-1
    if iguales==(int(len(num)/2)):
        print("LIMON")
    else:
        print("OK")
