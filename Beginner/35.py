'''
Diseña un programa que pida el valor del lado de un cuadrado y muestre el valor de su perimetro y el de su área
(prueba que tu programa funciona correctamente con este ejemplo: si el lado vale 1.1, el perímetro será 4.4, y el 
área 1.21 )
'''

lado = float (input("ingresa el valor del lado: ")) #convertimos el valor registrado en float y asi no usamos linea 8
#lado = float(lado)
area = lado*lado
perim=  lado *4
print("El área es: ", area, '\n'+"El perímetro es: ", perim)

