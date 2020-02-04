import sys
import math

def es_entero(n):
    try:
        _, p_decimal = str(n).split('.')
    except:
        return True
    return p_decimal == '0'

def es_especial(n):
    # n = n2**2 + n3**2
    #Fijamos primero n2 y comprobamos que n3 sea un número entero
    for n2 in range(1,math.ceil((n-1)**(1/2))):
        n3 = (n-n2**2)**(1/2)
        if ((n3 > 0) & es_entero(n3) & (n2 != n3)):
            return True
    return False

def es_primo(n):
    if n==1:
        return False
    
    for n2 in range(2,math.ceil(n/2)+1):
        if (n%n2 == 0):
            return False
    return True

n = int(sys.stdin.readline())
for linea in range(n):
    k = int(sys.stdin.readline())

    if (es_primo(k)):
        if (es_especial(k)):
            print("ESPECIAL")
        else:
            print("PRIMO")
    else:
        print("NO")
