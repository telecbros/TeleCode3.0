import sys
import math

fact_pulg_to_mil = 25.4

def n_nines(n):
    _, p_decimal = str(n).split('.')
    num_nines = 0
    for i in range(len(p_decimal)):
        if p_decimal[i] != '9':
            break
        num_nines += 1
    return num_nines

N = int(sys.stdin.readline())
for caso in range(N):
    diag_pulg, ancho_pix, alto_pix = sys.stdin.readline().split()
    diag_pulg = float(diag_pulg)
    diag_mil = fact_pulg_to_mil * diag_pulg
    ancho_pix = int(ancho_pix)
    alto_pix = int(alto_pix)
    
    if (ancho_pix == 0):
        alto_mil = diag_mil
        ancho_mil = 0.0
    elif (alto_pix == 0):
        alto_mil = 0.0
        ancho_mil = diag_mil
    else:
        relacion = int(ancho_pix) / int(alto_pix)
        alto_mil = ((diag_mil**2) / (1 + relacion**2))**(1/2)
        ancho_mil = relacion * alto_mil

    if (n_nines(ancho_mil) >= 12):
        ancho_mil = math.ceil(ancho_mil)
    if (n_nines(alto_mil) >= 13):
        alto_mil = math.ceil(alto_mil)
    print(math.trunc(ancho_mil), end=" ")
    print(math.trunc(alto_mil))
