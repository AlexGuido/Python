'''
Diseña un programa que dibuje un cuadrado cuyo lado mida 200 pasos y otro cuadrado de lado 100 centrado en su interior.
El cuadrado exterior ha de ser de color rojo y el interior color azul
'''
from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(625,425)
pantalla.screensize(600,400)

tortuga=Turtle()
tortuga.pencolor('red') #pintamos las lineas de color rojo
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200) #Termina el primer cuadrado

tortuga.penup()#Levantamos el puntero para que este no marque el recorrido en la pantalla
tortuga.left(135) #giramos el puntero 
tortuga.forward(70.71067812) # calculamos la hipotenusa para que el cuadrado quede en el centro Raiz de (50² + 50²)
tortuga.pendown() #Bajamos el puntero para dibujar el proximo cuadrado

tortuga.pencolor('blue') #pintamos las lineas de color azul
tortuga.right(45) #Empieza el segundo cuadrado 
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick() #Termina el programa haciendo click en la pantalla
