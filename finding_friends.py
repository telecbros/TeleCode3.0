import sys

def per_coin(bit_str1, bit_str2):
    no_coincide = bin(int(bit_str1, 2) ^ int(bit_str2, 2)).count("1")
    coincide = len(bit_str1) - no_coincide
    return coincide / len(bit_str1)

def search_coin(first_id, keys, per_preg):
    per = 0.5
    ident = -1
    for id in keys:
        if (id == first_id):
            continue
        percoin = per_coin(per_preg[first_id], per_preg[id])
        if ((percoin == per and id < ident) or (percoin > per)):
            per = percoin
            ident = id
    return ident

per_preg = {}

N, K = sys.stdin.readline().split()
N = int(N)
K = int(K)
for case in range(N):
    line = sys.stdin.readline()
    if "\n" in line:
        line = line[:-1]
    
    id, respuestas = line.split()
    id = int(id)
    per_preg[id] = respuestas

keys = list(per_preg.keys())
keys.sort()
while(len(keys) != 0):
    print(keys[0], end=" ")
    for i in range(3):
        id = search_coin(keys[0], keys, per_preg)
        if id == -1:
            break
        else:
            print(id, end=" ")
            keys.remove(id)
    keys.remove(keys[0])
    print()
