'''
Haz un programa que pida al usuario una cantidad de euros, una tasa de interés y un número de años. Muestra por pantalla
en cuánto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica una tasa de interés 
reducida. Recuerda que un capital de C euros a un interés del x por cien durante n años se convierte en C(1+x/100)^n euros.

(Prueba tu programa sabiendo que una cantidad de 10,000 euros al 4.5% de interés anual se convierte en 24,117.14 euros 
al cabo de 20 años)
'''

euros=float(input("Ingresa la cantidad de Euros: "))
interes=float(input("Ingresa la tasa de interés: "))
anios=float(input("Ingresa el número de años: "))

#formula:
capitalFinal= euros*(1+(interes/100))**anios
print("Al cabo de ", anios, "Tendrás: ",capitalFinal, "euros")
