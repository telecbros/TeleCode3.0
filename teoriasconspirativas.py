num_casos = int(input())

"""def es_primo(x): 
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
            return True"""

def es_primo(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True
            
def es_especial(num):
    if num < 2:
        return False
    for i in range(int(num**(1/2))):
        for j in range(int(num**(1/2))+1):
            if(i**2 + j**2 > num):
                break
            if(i**2 + j**2 == num):
                return True
    return False
    
            

for i in range(0,num_casos):
    dato = int(input())
    if(not es_primo(dato)):
        print("NO")
    elif(es_especial(dato) and es_primo(dato)):
        print("ESPECIAL")
    else:
        print("PRIMO")
        
    
