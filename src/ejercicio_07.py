import random
def realizar_sorteo(participantes):
    #Separa a los participantes por "," y saca los espacios
    miembros=[nombre.strip() for nombre in participantes.split(",")]

    if len(miembros)<3:
        return "Debe haber al menos 3 participantes"

    #Pasa la lista de los miembros a minuscula
    minuscula=[p.lower() for p in miembros]

    #El set saca valores duplicados, si no es igual al largo de la lista es porque hay algun duplicado
    if len(minuscula) != (len(set(minuscula))):
        return "Hay nombres duplicados"
    
    asignados=miembros.copy()

    while True:
        random.shuffle(asignados)
        valido=True
        #Si la persona asignada es el mismo se vuelve a mezclar
        for i in range(len(miembros)):
            if miembros[i]==asignados[i]:
                valido=False
                break
        #Si todas las personas tienen alguien asignado termina el while
        if valido:
            break
    
    #Combina las dos listas de miembros con su asignado
    resultado=zip(miembros,asignados)
    
    return resultado