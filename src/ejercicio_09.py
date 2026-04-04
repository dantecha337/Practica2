def limpiar_datos(students):
    alumnos={}
    for alumno in students:
        name=alumno["name"]
        grade=alumno["grade"]
        status=alumno["status"]

        #Si no tiene nombre o son solo espacios lo continua al siguiente alumno
        if not name or not name.strip():
            continue
        
        #Si esta vacio o la nota no es un numero continua al siguiente alumno
        if not grade or not grade.isdigit():
            continue

        #Pasa el nombre y el estado a formato titulo
        name=name.strip().title()
        status=status.strip().title()
        grade=int(grade)

        #Si es la primera vez que aparece o la nota actual es mayor que la anterior entonces lo agrega a la lista final
        if name not in alumnos or grade>alumnos[name]["grade"]:
            alumnos[name]={
                "grade":grade,
                "status":status
            }
        
    #Ordena el diccionario por nombre
    alumnos_ordenados=dict(sorted(alumnos.items()))

    return alumnos_ordenados