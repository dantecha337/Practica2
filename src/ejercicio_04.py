def validar_email(email):
    email=email.strip()
    valido=False
    #Si tiene un @ y no empieza con @ ni . (Verificacion extra que no tenga espacios dentro del email)
    if (email.count("@")==1 and 
        not " " in email and
        not email.startswith("@") and 
        not email.endswith("@") and 
        not email.startswith(".") and 
        not email.endswith(".")
        ):

        #Separa el email antes y despues del arroba
        arroba=email.split("@")

        #Verifica que haya al menos un caracter antes del arroba y que haya al menos un . despues del arroba (Verificacion extra que tenga al menos un caracter despues del @ y antes del .)
        if len(arroba[0])>=1 and "." in arroba[1] and not arroba[1].startswith("."):

            #Separa los puntos despues del arroba
            punto=arroba[1].split(".")

            #Comprueba que haya al menos 2 letras despues del ultimo punto
            if len(punto[-1])>=2:
                valido=True

    return valido
