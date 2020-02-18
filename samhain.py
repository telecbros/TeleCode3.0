# Puntos 814.35

num_brujas = int(input())
ingredientes = {}
ok = False

for i in range(0,num_brujas):
    linea = input()
    datos = linea.split(" ")
    if (datos[0] == "a"):
        if datos[1] in ingredientes:
            ingredientes[datos[1]] = int(ingredientes.get(datos[1])) + 1;
        else:
            ingredientes[datos[1]] = 1;
    if (datos[0] == "q"):
        ingredientes[datos[1]] = int(ingredientes.get(datos[1])) - 1;
    if (datos[0] == "b"):
        if datos[1] in ingredientes and int(ingredientes.get(datos[1])) > 0 :
            if(ok):
                print(" ", end="");
            print(str(i),end="");
            ok = True;

