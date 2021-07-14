from functools import reduce

lista = [1, 3, -1, 15, 9]

def doble(x):
    return x + x

listaDobles = map(lambda x: x*2, lista) # Es lo mismo

listaDobles1 = map(doble, lista) # Es lo mismo


def esPar(x):
    return x % 2 == 0


listaPares = filter(lambda x: x % 2 == 0, lista) # Es lo mismo

listaPares1 = filter(esPar, lista) # Es lo mismo


sumatorio = reduce(lambda x, y: x + y, lista)
sumatorioDobles = reduce(lambda x, y: x + y*2, lista)

suma100 = reduce(lambda x,y: x + y, range(101))

print(list(listaPares))
print(list(listaPares1))
print(list(listaDobles))
print(list(listaDobles1))
print(sumatorio)
print(sumatorioDobles)
print(suma100)




