# 1. Registrar usuario
print("EL juego del Ahorcado")
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre}. Buena suerte!")

# 2. Seleccionar palabra secreta
palabra_secreta = "ciberseguridad".lower()
palabra_mostrada = ["_"] * len(palabra_secreta)
intentos_restantes = 6

print("\n¡Comencemos el juego!")
print(" ".join(palabra_mostrada))
