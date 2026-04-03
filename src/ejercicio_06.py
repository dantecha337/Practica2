from collections import Counter


def analizar_hashtags(posts):
    
    hashtags=[]
    for post in posts:
        palabras=post.split()
        #Para cada palabra en cada post comprueba si empieza con #
        for palabra in palabras:
            if palabra.startswith("#"):
                hashtags.append(palabra)
    
    contador=Counter(hashtags)

    return contador