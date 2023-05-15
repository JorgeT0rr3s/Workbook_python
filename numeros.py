"""crear un programa que resiba una lista de numeros y 
    calcule la suma de los mismos usando un ciclo for"""
x = 0
listanumeros=[]
while len(listanumeros) < 5:
    numeros = int (input('ingrese 5 numeros enteros: '))
    listanumeros.append(numeros)

for i in listanumeros:
    x =x+i
print (x)
print (listanumeros)

