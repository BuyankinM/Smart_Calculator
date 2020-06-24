def tracklist(**kwargs):
    for group, songs in kwargs.items():
        print(group)
        for album, song in songs.items():
            print(f"ALBUM: {album} TRACK: {song}")