from Funciones1nivel import sumaTodos

print(sumaTodos(3,lambda x: x*2))

# Esto es lo mismo:

doble = lambda x: x*2
triple = lambda x: x*3

print(sumaTodos(3, doble))
print(sumaTodos(100, triple))


