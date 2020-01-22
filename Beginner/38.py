'''
Diseña un programa que pida el valor de los tres lados de un triangulo y calcule el valor de su área y perímetro.
Recuerda que el área A de un triangulo puede calcularse a partir de sus tres lados, a ,b c, así: A = sqrt[s(s-a)(s-b)(s-c)], 
donde s = (a+b+c)/2. (Prueba que tu programa funciona correctamente con este ejemplo: si los lados miden  3,5 y 7, el 
perímetro será 15.0 y el área 6.495190052838)
'''

from math import *

a=float(input("Ingresa el lado A: "))
b=float(input("Ingresa el lado B: "))
c=float(input("Ingresa el lado C: "))

s = (a+b+c)/2
area = sqrt((s*(s-a)*(s-b)*(s-c)))
perimetro = 2*s
print("El área del triangulo es: ",area, '\n' + "El perímetro es: ", perimetro)

