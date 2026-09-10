print("===== MUSIC PLAYLIST MANAGER =====")

playlist = []

while True:
    print("\n1. Add song")
    print("2. Remove song")
    print("3. View playlist")
    print("4. Search song")
    print("5. Show song count")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter song name: ")
        artist = input("Enter artist name: ")

        if song.strip() == "" or artist.strip() == "":
            print("Song and artist cannot be empty ❌")
        else:
            playlist.append({
                "song": song,
                "artist": artist
            })
            print("Song added to playlist! 🎵")

    elif choice == "2":
        song = input("Enter song to remove: ")
        found = False

        for music in playlist:
            if music["song"].lower() == song.lower():
                playlist.remove(music)
                print("Song removed! 🗑️")
                found = True
                break

        if not found:
            print("Song not found ❌")

    elif choice == "3":
        if not playlist:
            print("Playlist is empty.")

        else:
            print("\n===== MY PLAYLIST =====")

            for number, music in enumerate(playlist, start=1):
                print(
                    f"{number}. {music['song']} "
                    f"- {music['artist']}"
                )

    elif choice == "4":
        search = input("Enter song name to search: ")
        found = False

        for music in playlist:
            if search.lower() in music["song"].lower():
                print(
                    f"🎵 {music['song']} - "
                    f"{music['artist']}"
                )
                found = True

        if not found:
            print("No matching song found ❌")

    elif choice == "5":
        print(f"Total songs: {len(playlist)} 🎶")

    elif choice == "6":
        print("Playlist closed. Bye! 👋")
        break

    else:
        print("Invalid choice ❌")