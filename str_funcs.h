//Sustituye el último char de una string
void sustlchr(char *ptr, char oldchr, char newchr);

//Sustituye todos los chars de una palabra
void sustchr(char *str, char oldchr, char newchr);

//Devuelve el nº de veces que aparece c en str
int nchr(char *str, char c);

//Elimina los últimos espacios vacios de la string
void rm_lspaces(char *ptr);

//Devuelve una nueva string con los primeros espacios vacios eliminados
char *rm_fspaces(char *ptr);

//Devuelve una nueva string con los espacios sobrantes quitados (primeros y últimos)
char *rm_spaces(char *str);

//Convierte un int en una string (len es la memoria que se reserva para la string)
char *itoc(int i, int len);

//Replaces the first occurrence of oldstr by newstr
void replace(char **line, char *oldstr, char *newstr, int len);

//Retorna 1 si word es la primera palabra de str. 0 en caso contrario
int is_fword(char *str, char *word);

//Retorna 1 si word es la última palabra de str. 0 en caso contrario
int is_lword(char *ptr, char *word);

//Elimina la última palabra de string
void rm_lword(char *ptr);

char* char_to_string(char c);

/* Splitea en base a un delimitador. Retorna un puntero que apunta 
a un array de string (punteros de tipo char).
IMPORTANTE: El último elemento del array contiene un null para
detectar el final del array.*/
char** split(char* str, char delimiter);
