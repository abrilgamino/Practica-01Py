from ast import Div, If
from audioop import mul
from re import sub


numero1 = 2
numero2 =4

mul = numero1 *numero2
sum = numero1 + numero2
sub = numero2 - numero1
div = numero2 / numero1


print(mul)
print(sum)
print(sub)
print(div)


numero1 += numero2

mul = numero1 *numero2
sum = numero1 + numero2
sub = numero2 - numero1
div = numero2 / numero1


print(mul)
print(sum)
print(sub)
print(div)

Edad = 25
EdadLegal = 18
Resultado = "Eres mayor de edad" if Edad >= EdadLegal else "Eres menor de edad"
print(Resultado)

