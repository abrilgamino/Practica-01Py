secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")


# Indicar al usuario que ingrese un número entero.

user_number=int(input('Ingresa el numero: '))

# Escribir un bucle while y el resto de tu código.

while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Ingresa el número nuevamente: "))
print(secret_number, "¡Bien hecho, muggle! Eres libre ahora.")

