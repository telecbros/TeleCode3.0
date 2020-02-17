def n_nines(n):
    _, p_decimal = str(n).split('.')
    num_nines = 0
    for i in range(len(p_decimal)):
        if p_decimal[i] != '9':
            break
        num_nines += 1
    return num_nines
