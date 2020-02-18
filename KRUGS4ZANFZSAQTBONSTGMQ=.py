# Puntos 150.0

import base64

num = int(input())
for n in range (0,num):
    frase = str(input())
    frase=(str(base64.b32decode(frase)))
    frase = frase.split("'")
    print(frase[1])
    
