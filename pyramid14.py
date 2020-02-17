import sys

def major_that(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    
    if(len(n1) < len(n2)):
        end_index = len(n1)
    else:
        end_index = len(n2)
    
    for i in range(end_index):
        if (int(n1[i]) > int(n2[i])):
            return True
        elif (int(n1[i]) < int(n2[i])):
            return False
    
    if(len(n1) > len(n2)):
        return True
    else:
        return False

piramides = {}
bloques_tot = 0
bloques_to_print = 0
altura_to_print = 0
M = int(sys.stdin.readline())
for cliente in range(M):
    N = int(sys.stdin.readline())
    bloques = N*N
    bloques_tot += bloques
    if major_that(bloques, bloques_to_print):
        bloques_to_print = bloques
        altura_to_print = N
print(bloques_tot)

spaces = altura_to_print-1
for l in range(altura_to_print):
    asterix = 1 + l*2
    print(" "*spaces + "*"*asterix)
    spaces -= 1

print(bloques_to_print)
