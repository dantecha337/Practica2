def analizar_playlist(playlist):
    total_seconds=0
    max_song=None
    min_song=None

    max_duration=0
    min_duration=9999

    for song in playlist:
        #Separa minutos y segundos con el :
        minutes, seconds=song["duration"].split(":")

        duration_seconds=int(minutes)*60+int(seconds)

        total_seconds+=duration_seconds

        #Verifica cancion mas larga
        if duration_seconds>max_duration:
            max_duration=duration_seconds
            max_song=song
        
        #Verifica cancion mas corta
        if duration_seconds<min_duration:
            min_duration=duration_seconds
            min_song=song

    print(f'duracion total: {total_seconds//60}m {total_seconds%60}s')
    print(f'Cancion mas larga: "{max_song["title"]}" {max_song["duration"]}')
    print(f'Cancion mas corta: "{min_song["title"]}" {min_song["duration"]}')