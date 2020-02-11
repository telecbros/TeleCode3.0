#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// -------------- ARRAY DE ENTEROS ----------- //
struct Int_Array{
    int* int_arr;
    int len;
};
typedef struct Int_Array IA;


// -------------- LISTA ARRAY DE ENTEROS ----------- //
struct List_Int_Array_a{
    IA* int_arr;
    struct List_Int_Array_a* next;
};
typedef struct List_Int_Array_a List_IA_a;

struct List_Int_Array{
    List_IA_a* first;
    int n_elements;
};
typedef struct List_Int_Array List_IA;
