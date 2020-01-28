import sys

marmita = {}
brujas_fail = []
brujas_beben = 0

def añadir(cosa):
    try:
        marmita[cosa] = marmita[cosa] + 1
    except KeyError:
        marmita[cosa] = 1

def eliminar(cosa):
    try:
        n_cosas = marmita[cosa]
    except KeyError:
        return
    
    if n_cosas > 1:
        marmita[cosa] = marmita[cosa] - 1
    else:
        del marmita[cosa]

num_brujas = int(sys.stdin.readline())

for cont in range(num_brujas):
    letra, cosa = sys.stdin.readline().split()
    
    if (letra == 'a'):
        añadir(cosa)
    elif (letra == 'q'):
        eliminar(cosa)
    elif (letra == 'b'):
        brujas_beben = brujas_beben + 1
        if cosa in marmita:
            brujas_fail.append(cont)
    cont = cont + 1
