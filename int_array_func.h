#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void init_IA(IA* p_ia, int len_arr);

IA* int_array_copy(IA int_arr);

/* Function to calculate permutations of int array
   This function takes three parameters: 
   1. array 
   2. Starting index of the array 
   3. Ending index of the array.
   4. Lista donde se guardan las permutaciones*/
void permute(IA* a, int l, int r, List_IA* p_list);

void print_int_arr(IA arr);
