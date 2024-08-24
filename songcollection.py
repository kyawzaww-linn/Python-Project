"""..."""

import json
from song import Song


class SongCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs

    def get_learned_songs(self):
        return [song for song in self.songs if song.learned]

    def get_unlearned_songs(self):
        return [song for song in self.songs if not song.learned]

    def load_songs(self, file_name):
        with open(file_name, 'r') as file:
            songs = json.load(file)
            for song_dict in songs:
                title = song_dict.get('title', 'Unknown Title')
                artist = song_dict.get('artist', 'Unknown Artist')
                year = song_dict.get('year', 0)
                learned = song_dict.get('learned', False)  # Default value if 'learned' key is missing
                song = Song(title, artist, year, learned)
                self.songs.append(song)

    def save_songs(self, filename):
        with open(filename, 'w') as file:
            song_data = [{'title': song.title, 'artist': song.artist, 'year': song.year, 'learned': song.learned} for
                         song in self.songs]
            json.dump(song_data, file, indent=4)
