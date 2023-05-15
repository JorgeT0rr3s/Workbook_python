"""Crear un programa que reciba una lista de palabras y
muestre únicamente aquellas que empiezan con una letra
determinada, utilizando un ciclo for y una estructura
condicional if"""


lista=[]

while len(lista) < 5:
    palabras = str(input('ingrese 5 palabras: '))
    lista.append(palabras)

for i in lista:
    if i[0] == 'a':
        print (i)
print(lista)
