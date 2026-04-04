import string


def cifrar_mensaje(mensaje, desplazamiento):
    resultado= ""
    
    for letra in mensaje:
        if letra.isalpha():

            es_mayus=letra.isupper()
            letra=letra.lower()

            #Calcula el movimiento de la letra con los valores ASCII y con el mod vuelve al inicio cada vez que llega a la z
            indice= ord(letra) - ord('a')
            nuevo_indice=(indice+desplazamiento) % 26

            #Se desplaza la cantidad calculada y lo pasa a caracter de vuelta
            letra_cifrada= chr(nuevo_indice + ord('a'))

            if es_mayus:
                letra_cifrada=letra_cifrada.upper()
            
            resultado+=letra_cifrada
        
        #Si no es una letra se mantiene igual
        else:
            resultado+=letra
    
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)
