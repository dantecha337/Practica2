def filtrar_spoilers(text, spoilers):

    words = [p.strip().lower() for p in spoilers.split(",") if p.strip()]
    
    result = text
    
    for spoiler in words:
        
        #Donde inicia la palabra para saber desde donde censurar
        inicio = 0

        while True:

            # Busca el spoiler en minuscula 
            pos = result.lower().find(spoiler, inicio)
            
            if pos == -1: # Si ya no hay más coincidencias de esta palabra
                break
            
            # Calcula la longitud de la palabra y calcula la longitud de la censura por *
            largo = len(spoiler)
            censura = "*" * largo
            
            # Agrega la censura sumando sin tocar ni antes ni despues de esta
            result = result[:pos] + censura + result[pos + largo:]
            
            # Mueve el índice de inicio para seguir buscando después del reemplazo
            inicio = pos + largo
            
    return result