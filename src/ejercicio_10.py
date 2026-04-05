def simular_competencia(rounds):
    

    #Crea un diccionario con los nombres como claves y como valor otro diccionario con total de puntos, rondas ganadas y mejor ronda
    tabla_final={p:{"total":0, "rondas_ganadas":0,"puntaje_max":0} for p in rounds[0]["scores"]}
    
    i=0
    #Por cada ronda
    for ronda in rounds:

        puestos = []
        #Por cada participante
        for participante, jueces in ronda["scores"].items():
        
            #Suma las notas
            puntaje=sum(jueces.values())
            
            #Guarda el puntaje de cada uno
            puestos.append((puntaje,participante))

            #Va sumando los puntos de cada ronda al total
            tabla_final[participante]["total"]+=puntaje

            #Comprueba si el puntaje de la ronda es el mejor hasta ahora
            if puntaje>tabla_final[participante]["puntaje_max"]:
                tabla_final[participante]["puntaje_max"]=puntaje
        
        #Ordena los puntajes
        puestos = sorted(puestos, reverse=True)

        #Le suma una ronda ganada al que gano 
        tabla_final[puestos[0][1]]["rondas_ganadas"]+=1
        
        
        i+=1
        #Imprime ganador de la ronda y tabla de posiciones
        print(f"Ronda {i} - {ronda['theme']}:")
        
        ganador_puntaje, ganador_nombre=puestos[0]
        print(f"\tGanador: {ganador_nombre} ({ganador_puntaje} pts)")
        
        for p in range(1,len(puestos)):
            puntaje, nombre=puestos[p]
            print(f"\tPuesto {p+1}: {nombre} ({puntaje} pts)")

    #De cada elemento de la tabla final agarra el valor y del valor agarra el total de puntos y lo ordena en base a eso 
    tabla_final_ordenada=dict(sorted(tabla_final.items(), key=lambda x:x[1]["total"], reverse=True))
    return tabla_final_ordenada

def calcular_promedio(puntaje, rondas):
    return puntaje/rondas
        
