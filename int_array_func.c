#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void init_IA(IA* p_ia, int len_arr){
    p_ia->int_arr = malloc(sizeof(int)*len_arr);
    p_ia->len = len_arr;
}

IA* int_array_copy(IA int_arr){
    int i;
    IA* result = malloc(sizeof(IA));
    result->int_arr = malloc(sizeof(int)*int_arr.len);
    result->len = int_arr.len;
    
    for (i=0; i<int_arr.len; i++){
        result->int_arr[i] = int_arr.int_arr[i];
    }
    return result;
}

/* Function to calculate permutations of int array
   This function takes three parameters: 
   1. array 
   2. Starting index of the array 
   3. Ending index of the array. */
void permute(IA* a, int l, int r, List_IA* p_list)
{
    int i; 
    if (l == r){
        add_List_IA(p_list, int_array_copy(*a));
    }else{ 
       for (i = l; i <= r; i++) { 
          swap((a->int_arr+l), (a->int_arr+i));
          permute(a, l+1, r, p_list); 
          swap((a->int_arr+l), (a->int_arr+i)); //backtrack 
       } 
    } 
}

void print_int_arr(IA arr){
    int i;
    for(i = 0; i<arr.len; i++){
        printf("%d ", arr.int_arr[i]);
    }
    printf("\n");
}
