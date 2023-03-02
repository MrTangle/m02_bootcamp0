from functools import reduce

lista = [1, 3, -1, 15, 9]

def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor

    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor*2

    return resultado

def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor

    return resultado

def doble(x):
    return x + x

listaDobles1 = map(doble, lista)
#Lo mismo, pero con lambda
listaDobles = map(lambda x: x*2, lista)


def esPar(x):
    return x % 2 == 0

listaPares1 = filter(esPar, lista)
#Lo mismo, pero con lambda
listaPares = filter(lambda x: x % 2 == 0, lista)

sumatorio = reduce(lambda x, y: x + y, lista)
sumatorioDobles = reduce(lambda x, y: x + y*2, lista)

suma100 = reduce(lambda x, y: x+y, range(101))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)


