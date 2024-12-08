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
# 3.Comienza el juego
while intentos_restantes > 0:
    # Adivinar letra
    letra = input("\nAdivina una letra: ").lower()
    
    if letra in palabra_secreta:
        print("Correcto!")
        # Actualizar las posiciones de las letras adivinadas
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_mostrada[i] = letra
    else:
        print("Incorrecto. Pierdes un intento.")
        intentos_restantes -= 1

#EXPLICACION DEL PROCEDIMIENTO:
# se utilizara el comando "while" meintras tengamos los intentos restantes
# dentro del ciclo se pide al jugador que adivine una letra la cual se almacenara
# en la variable "letra". Por medio de la funcion .lower convertiremos las letras escritas
# en minusculas. Utilizaremos la condicion "IF" para verificar si la letra adivinada es correcta
# si la letra esta en la palbra secreta se imprimira el mensaje "correcto"
# Utilizaremos el comando "bucle For" para recorrec la posicion de la palabra secreta

