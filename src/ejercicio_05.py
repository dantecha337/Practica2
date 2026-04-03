def calcular_costo(peso, destino):
    
    #Calcula el rango de peso
    if peso <= 1:
        i = 0
    elif peso <= 5:
        i = 1
    else:
        i = 2

    match destino.lower():
        #Precios para cada destino dependiendo del peso
        case "local":
            precios=[500,1000,2000]
        case "regional":
            precios=[1000,2500,5000]
        case "nacional":
            precios=[2000,4500,8000]
        case _:
            return None
    #Devuelve segun el indice del peso
    return precios[i]