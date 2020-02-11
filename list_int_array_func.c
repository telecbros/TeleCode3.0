#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void init_List_IA(List_IA* p_list){
    p_list->first = NULL;
    p_list->n_elements = 0;
}

void add_List_IA(List_IA* p_list, IA* int_arr){
    List_IA_a* node = malloc(sizeof(List_IA_a));
    node->int_arr = int_arr;
    node->next = p_list->first;
    p_list->first = node;
    p_list->n_elements++;
}

void print_List_IA(List_IA list){
    if (list.n_elements == 0){
        return;
    }
    
    List_IA_a* aux = list.first;
    do{
        print_int_arr(*(aux->int_arr));
        aux = aux->next;
    }while (aux != 0);
}
