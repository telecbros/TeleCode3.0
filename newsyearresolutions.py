# Puntos 150.0

import math

num_casos = int(input())

def calcular_diagonal(ancho, alto):
    return (ancho**2 + alto**2)**(1/2)

def calcular_ppp(dia, pulgadas):
    return dia/pulgadas

def tamaño_ancho(ppp, ancho):
    return (ancho/ppp)*25.4

def tamaño_alto(ppp, alto):
    return (alto/ppp)*25.4

for i in range(num_casos):
    medidas = input()
    datos = medidas.split(" ")
    diagonal_pixel = calcular_diagonal(float(datos[1]), float(datos[2])) # diagonal en pixeles
    ppp = calcular_ppp(diagonal_pixel,float(datos[0])) # ppp
    ancho = str(int(tamaño_ancho(ppp,float(datos[1]))))
    ancho = ancho.split(".")
    alto = str(int(tamaño_alto(ppp,float(datos[2]))))
    alto = alto.split(".")
    print(ancho[0] + " " + alto[0])
