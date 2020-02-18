# Puntuacion 0.0

num_mensajes = int(input())
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ"+" ",range(27)))
I2L = dict(zip(range(27),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ " "))
plaintext_s = "AS" + " "
ciphertext_s = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]
for key in range(0,27): 
        #encipher
        for c in plaintext_s.upper(): 
            ciphertext_s[key] += I2L[(L2I[c] + key)%27]
                
for i in range(num_mensajes):
    frase = input()
    for key in range(0,27):
        if ciphertext_s[key] not in frase:
            continue
        #decipher
        plaintext2 = ""
        for c in frase.upper():
            plaintext2 += I2L[ (L2I[c] - key)%27]     
        print(plaintext2)
