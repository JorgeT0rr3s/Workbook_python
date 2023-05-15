"""Crear un programa que reciba dos listas de números y
que genere una tercera lista que contenga la suma de
los elementos de las dos listas en la misma posición,
utilizando un ciclo for."""

lista1=[]
lista2=[]
listasuma=[]
while len(lista1) < 5:
    num1 = int (input('ingrese 5 numeros enteros: '))
    lista1.append(num1)

while len(lista2) < 5:
    num2 = int (input('ingrese  otros 5 numeros enteros: '))
    lista2.append(num2)
print(lista1)
print(lista2)
for i in range(len(lista1)):
    listasuma.append(lista1[i]+lista2[i])

print(listasuma)

