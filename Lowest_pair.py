import sys

#Algoritmo para encontrar pares
def find_pairs(x):
    pairs = [[1,x]]
    final_val = x**(1/2)
    if (x%2 != 0):
        increment = 2
        i =3
    else:
        increment = 1
        i = 2

    while (i <= final_val):
        if (x%i == 0):
            pairs.append([i,x/i])
        i = i + increment
    return pairs
            
T = int(sys.stdin.readline())
for case in range(T):
    num = int(sys.stdin.readline())
    pairs = find_pairs(num)
    lowest_pair = pairs[len(pairs)-1]

    for n in lowest_pair:
        print(int(n), end = " ")
    print()
