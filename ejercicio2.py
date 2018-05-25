# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)

a=0
i=0
while (i==0):
    a=a+1
    if(x[a]>800):
        i=1
    if(x[a]%2!=0 and x[a]<800):
        print(x[a])
    


