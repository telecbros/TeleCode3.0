import sys
import math

def es_entero(n):
    try:
        _, p_decimal = str(n).split('.')
    except:
        return True
    return p_decimal == '0'

def is_capicua(num):
    if len(num) % 2 == 0:
        l = num[:int(len(num)/2)]
        r = num[int(len(num)/2):]
    else:
        l = num[:int(math.floor(len(num)/2))]
        r = num[int(math.floor(len(num)/2))+1:]
    return l == r[::-1]
    
    

N = int(sys.stdin.readline())
for case in range(N):
    num = sys.stdin.readline()
    if "\n" in num:
        num = num[:-1]

    if (is_capicua(num)):
        print("LIMON")
    else:
        print("OK")
