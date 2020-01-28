import sys

def good_shift(pre, nex):
    good = False
    shift = 1
    #infinite loop
    while 0 == 0:
        shift_result = pre >> shift
        if (nex == shift_result):
            good = True
            break
        if (shift_result == 0):
            break
        shift = shift + 1
    return good

def case_good():
    good = True
    first_round = True

    #infinite loop
    while 0 == 0:
        if first_round:
            prev_num = int(sys.stdin.readline())
            first_round = False
            
        if (prev_num == 0):
            break
        
        next_num = int(sys.stdin.readline())
        #if (next_num != prev_num >> 1 & next_num != prev_num):
        n_ones_prev = bin(prev_num).count("1")
        n_ones_next = bin(next_num).count("1")
        
        if (next_num > prev_num):
            good = False
        if not good_shift(prev_num, next_num):
            good = False
        prev_num = next_num

    return good

n_testcases = int(sys.stdin.readline())
for case in range(n_testcases):
    if (case_good()):
        print("GANADORES")
    else:
        print("DESCALIFICADOS")
