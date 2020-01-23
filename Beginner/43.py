'''
Diseña un programa que dibuje un triángulo equilatero con la tortuga.
'''

from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

tortuga=Turtle()
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
pantalla.exitonclick()
