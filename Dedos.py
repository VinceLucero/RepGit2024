
def encuesta():
    respuesta = input("¿Tienes alguna discapacidad? (Responde 'Si' o 'No'): ")
    if respuesta.lower() == 'si':
        respuesta_brazos = input("¿Te faltan ambos brazos? (Responde 'Si' o 'No'): ")
        if respuesta_brazos.lower() == 'si':
            return False
        else:
            respuesta_dedos = input("¿Tienes más de dos dedos? (Responde 'Si' o 'No'): ")
            if respuesta_dedos.lower() == 'si':
                return True
            else:
                return False
    else:
        return True

print("Hola, bienvenido a este repositorio. Te invitamos a contestar la siguiente encuesta, después te diremos qué hacer.")
if encuesta():
    print("Métete los dedos.")
else:
    print("Vete a la verga.")
