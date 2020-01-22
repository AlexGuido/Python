'''
El área de un triangulo se puede calcular a partir del valor de sus lados, a y b, y del ángulo tetha que estos forman entre si
con la fórmula A = (1/2)ab sin(tetha). Diseña un programa que pida al usuario el valor de los dos lados (en metros), y el ángulo 
que estos forman.
(Ten en cuenta que la función sin de python trabaja en radianes, así que el ángulo que leas en grados deberás pasarlo a radianes
sabiendo que pi radianes son 180 grados. Prueba que has hecho bien el programa introduciendo los siguientes datos: a= 1, b=2, 
tetha= 30; el resultado es 0.5)
'''

import math 

a=float(input("Ingresa el lado a: "))

b=float(input("Ingresa el lado b: "))

tetha=float(input("ingresa el ángulo tetha: "))

tetha = tetha*(math.pi)/180 #convertimos el ángulo en radianes 

A = float((1/2)*a*b*math.sin(tetha)) #área del triangulo

print("El área del triangulo es: ",A)

#prueba con git 
