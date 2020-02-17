import sys

marmita = []

num_brujas = int(sys.stdin.readline())
string = ""
for cont in range(num_brujas):
    letra, cosa = sys.stdin.readline().split()
    
    if (letra == 'a'):
        marmita.append(cosa)
    elif (letra == 'q'):
        if cosa in marmita:
            marmita.remove(cosa)
    elif (letra == 'b'):
        if cosa in marmita:
            print(cont, end=' ')
print()
