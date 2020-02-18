# Puntos 200.0

numero_casos = int(input())  

def es_primo(x): 
    if x<2:
        return False 
    elif x==2:
        return True
    else:
        objetivo = int(x**(1/2))
        if (objetivo >= 2):
            for n in range(2,objetivo+1):
                if x%n == 0:
                    return False
                elif(n == objetivo):
                    return True
        else:
            return True


for i in range(0,numero_casos):
    # Me hago un array que me guarde el resultado y los dos numeros que lo consiguen
    primera_vez = False
    result = [0,0,0]
    x = 2
    j = 2
    num = int(input())
    parar = num+1
    if(es_primo(num)):
        print(str(1) + " " + str(num))
        continue
    while j <= parar:
        if(j>=parar):
            break
        for x in range(2,parar):
            if(int(j)*int(x)>num): 
                break
            if((int(j)*int(x))==num and not primera_vez):
                result = [int(j)+int(x),j,x]
                primera_vez = True
            if((int(j)*int(x))==num):
                if(j+x < result[0]):
                    result = [int(j)+int(x),j,x]
        j = j+1
    print(str(result[1]) + " " + str(result[2]))
