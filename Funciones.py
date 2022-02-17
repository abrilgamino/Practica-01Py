def printHello (firstname, secondname):
 print('Hola', firstname, secondname)
printHello (firstname = ' Abril', secondname= 'Gamiño')
printHello('Gamiño', 'Abril')

def expedirINE (name, edad=18):
    print('INE de', name, edad)
expedirINE('Abril')

print('****************')

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)


def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")

value = None
if value is None:
    print("Lo siento, no contienes ningún valor")