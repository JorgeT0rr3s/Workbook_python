"""Crea un programa que le pida al usuario que ingrese un número entero.
Si el número es par, imprime "El número es par".
Si el número es impar, imprime "El número es impar".
"""

X = int(input("ingrese un numero entero"))

if X % 2 == 0:
    print ("el numero ingresado es par")
else:
    print("el numero ingresado es impar")
