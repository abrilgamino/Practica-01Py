#Es mutable- puede cambiar su valor. En consecuencia no mutable es que no puede cambiar el estado de su valor

registroNombreLista= ("Abril", "Michelle", "Gamiño")
registroNombre= ("Abril", "Michelle", "Gamiño")
'''
for value in registroNombre:
  print(value)
'''
#registroNombreLista[0]= "Abril"
#print(registroNombreLista[0])

nombre ='Abril'
strnumber1 = '1'
strnumber2 = '2'

print(strnumber1 + strnumber2)

print((strnumber1.isnumeric()if int(strnumber1)else strnumber1)+(strnumber2.isnumeric() if int(strnumber2)else strnumber2))

print(type(strnumber1)) 

for character in nombre:
  print(character)



