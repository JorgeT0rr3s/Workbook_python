
"""Crear un programa que reciba una cadena de caracteres y muestre cada letra en una
línea distinta utilizando un ciclo for."""

lista=[]
while len(lista) < 5:
    caracter = str (input('ingrese 5 caracteres: '))
    lista.append(caracter)

for i in lista:
    print (i)
