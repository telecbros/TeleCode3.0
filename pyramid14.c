// Puntuacion 1000.0

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

enum{
    MaxInt = 100,
};

struct Client{
    int height;
    int n_blocks;
};
typedef struct Client Client;

int num_imp (int pos)
{
    return 1+(pos-1)*2;
}

char* itoc(int i, int len)
{
    char *value;
    
    value = malloc(len);
    snprintf(value, len, "%d", i);
    return value;
}

int num_blocks (int height)
{
    return height * height;
}

void save_data (Client* client)
{
    char* line = malloc(MaxInt);
    int height;
    
    fgets(line, MaxInt, stdin);
    height = atoi(line);
    free(line);
    
    client->height = height;
    client->n_blocks = num_blocks(height);
}

long long sum_blocks (Client* client_list, int n_clients)
{
    int i;
    long long count = 0LL;
    
    for(i = 0; i < n_clients; i++){
        count = count + (long long)client_list[i].n_blocks;
    }
    return count;
}

int compare (int n1, int n2)
{
    char* num1;
    char* num2;
    
    num1 = itoc(n1, MaxInt);
    num2 = itoc(n2, MaxInt);

    return strcmp(num1, num2);
}

Client first_pyramic (Client* client_list, int n_clients)
{
    Client first_py;
    int i;
    
    first_py = client_list[0];
    for(i = 1; i < n_clients; i++){
        if(compare(client_list[i].n_blocks, first_py.n_blocks) >= 0){
            first_py = client_list[i];
        }
    }
    return first_py;
}

void print_n_char (char c, int n)
{
    int i;
    
    for(i=0; i<n; i++){
        printf("%c", c);
    }
}

void print_pyramic (Client client)
{
    int height = client.height;
    int n_blocks = client.n_blocks;
    int i;
    int spaces = height-1;
    
    for(i=1; i<=height; i++){
        print_n_char(' ', spaces);
        print_n_char('*', num_imp(i));
        spaces--;
        printf("\n");
    }
}

int main() {
    char* line = malloc(MaxInt);
    int n_clients;
    Client first_py;
    int i;
    
    fgets(line, MaxInt, stdin);
    n_clients = atoi(line);
    Client client_list[n_clients];
    free(line);
    
    for(i = 0; i < n_clients; i++){
        save_data(&client_list[i]);
    }
    
    printf("%lld\n", sum_blocks(client_list, n_clients));
    first_py = first_pyramic(client_list, n_clients);
    print_pyramic(first_py);
    printf("%d", first_py.n_blocks);
}

