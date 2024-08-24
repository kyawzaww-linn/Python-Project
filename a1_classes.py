"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to

"""Name:Kyaw Zaww Linn
Date started:18/12/23
GitHub URL:GET https://github.com/JCUS-CP1404/cp1404-song-list-assignment-1-kyawzawwlinn"""

import csv

# Constants
SONGS_FILE = 'songs.csv'
UNLEARNED = 'u'
LEARNED = 'l'
STATUS_INDEX = 3


def load_songs():
    try:
        with open(SONGS_FILE, 'r') as file:
            reader = csv.reader(file)
            return [song for song in reader]
    except FileNotFoundError:
        return []


def save_songs(song_list):
    with open(SONGS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(song_list)


def display_songs(song_list):
    if not song_list:
        print("No songs available.")
        return

    learned_count = sum(1 for song in song_list if song[STATUS_INDEX] == LEARNED)
    unlearned_count = len(song_list) - learned_count

    for i, song in enumerate(song_list, start=1):
        status = '*' if song[STATUS_INDEX] == UNLEARNED else ''
        print(f"{i}. {song[0]} - {song[1]} ({song[2]}){status}")

    print(f"\n{learned_count} songs learned, {unlearned_count} songs still to learn")


def get_valid_year():
    while True:
        year_input = input("Year: ")
        try:
            year = int(year_input)
            if year < 0:
                print("Number must be > 0.")
            elif year == 0:
                print("Number must be > 0.")
            else:
                return year
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be blank.")


def add_song(song_list):
    print("Enter details for a new song.")
    title = get_non_empty_input("Title: ")
    artist = get_non_empty_input("Artist: ")
    year = get_valid_year()

    song_list.append([title, artist, year, UNLEARNED])
    print(f"{title} by {artist} ({year}) added to the song list.")


def complete_song(song_list):
    unlearned_songs = [i for i, song in enumerate(song_list) if song[STATUS_INDEX] == UNLEARNED]

    if not unlearned_songs:
        print("No more songs to learn!")
        return

    while True:
        number = input("\nEnter the number of a song to mark as learned: ")

        if int(number) <= 0:
            print("Number must be > 0.")
        elif int(number) > len(song_list):
            print("Invalid song number")
        else:
            break

    index = int(number) - 1

    if song_list[index][STATUS_INDEX] == LEARNED:
        print(f"You have already learned {song_list[index][0]}")
    else:
        song_list[index][STATUS_INDEX] = LEARNED
        print(f"{song_list[index][0]} by {song_list[index][1]} learned")


def main():
    print("Song List 1.0 - by Kyaw Zaww Linn\n")
    songs = load_songs()
    print(f"{len(songs)} songs loaded.\n")

    while True:
        print("Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit\n")
        choice = input(">>> ").lower()

        if choice == 'd':
            display_songs(songs)
        elif choice == 'a':
            add_song(songs)
        elif choice == 'c':
            complete_song(songs)
        elif choice == 'q':
            save_songs(songs)
            print(f"\n{len(songs)} songs saved to {SONGS_FILE}\nMake some music!")
            break
        else:
            print("Invalid menu choice\n")


if __name__ == "__main__":
    main()
