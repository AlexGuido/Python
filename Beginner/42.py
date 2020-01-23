'''
Diseña un programa legible que solicite el radio de una circunferencia y muestre su área y perímetro con solo 2 decimales
'''
from math import pi

radio = float(input("Ingresa el Radio: "))

perimetro = 2*pi*radio
area =pi*radio**2

print("Perímetro: {0:.2f}".format(perimetro), "\n área: {0:.2f}".format(area)) #Sólo dos decimales


