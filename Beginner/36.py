'''
Diseña un programa que pida el valor de los lados de un rectangulo y muestre el valor de su perimetro y el de su área.
(prueba que tu programa funciona correctamente con este ejemplo: si un lado mide 1 y el otro 5, el perimetro será
12.0, y el área 5.0)
'''
ladoA = float(input("Ingresa el lado A del rectangulo: "))
ladoB = float(input("Ingresa el lado B del rectangulo: "))
area =  ladoA*ladoB
perim = 2*ladoA + 2*ladoB
print("El área del rectangulo es: ", area,'\n'+ "El perímetro es: ", perim)
