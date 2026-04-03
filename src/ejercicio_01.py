def analizar_zen_python(text):
    
    # Reemplazar saltos de línea por espacio
    text = text.replace("\n", " ")

    # Unificar finales de oración
    text = text.replace("!", ".").replace("?", ".")
    
    # Separar por punto
    lines = text.split(". ")

    #Cantidad de lineas
    total_lines=len(lines)

    #Total de palabras
    total_words=len(text.split())

    #Promedio de palabras por linea
    average=total_words/total_lines

    print(f"Total de lineas: {total_lines}")
    print(f"Total de palabras: {total_words}")
    print(f"Promedio: {average:.2f}")

    #Cuenta las palabras y compara con el promedio
    for line in lines:
      count=len(line.split())
      if count>average:
         print(f'- {line.strip()} ({count} palabras)')

