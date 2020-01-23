'''
Diseña un programa que dibuje un triangulo equilátero con la tortuga. El trazo del triangulo debe tener un grosor
de 10 píxels
'''

from turtle import Screen, Turtle

pantalla = Screen() #configuramos pantalla
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga=Turtle()
tortuga.pensize(10) #usamos el trazo de 10 pixels
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)

pantalla.exitonclick() #Salimos del programa con un click en la pantalla 
