import sys

def hay_camino(entrada, salida, dicc):
    try:
        vecinos = dicc[entrada]
    except KeyError:
        return False
    
    for vecino in vecinos:
        if vecino == salida:
            return True
    
    del dicc[entrada]
    
    for vecino in vecinos:
        if hay_camino(vecino, salida, dicc):
            return True
    return False
    

def resolver_caso():
    n_in_out = int(sys.stdin.readline())
    entrada, salida = sys.stdin.readline().split()
    entrada = int(entrada)
    salida = int(salida)
    
    dicc = {}
    for nodo in range(n_in_out):
        dicc[nodo] = sys.stdin.readline().split()
        dicc[nodo] = [int(i) for i in dicc[nodo]]
    
    return hay_camino(entrada, salida, dicc)
    

num_casos = int(sys.stdin.readline())
for caso in range(num_casos):
    sol = resolver_caso()
    if sol == True:
        print("SI!")
    else:
        print("NO!")
