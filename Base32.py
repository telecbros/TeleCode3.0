import sys
import base64

N = int(sys.stdin.readline())
for caso in range(N):
    s = sys.stdin.readline()[:-1] #Quito fin de línea
    bits = base64.b32decode(s)
    print(bits.decode())
