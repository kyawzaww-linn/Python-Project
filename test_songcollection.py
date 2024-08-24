""" Tests for SongCollection class. """
import json
import tempfile
from song import Song
from songcollection import SongCollection


def run_tests():
    """ Test SongCollection class. """

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs

    # Test adding a new Song with values
    print("Test adding new song:")
    song = Song("My Happiness", "Powderfinger", 1996, True)
    song_collection.add_song(song)
    assert song in song_collection.songs

    # Test getting learned and unlearned songs
    print("Test getting learned and unlearned songs:")
    unlearned_song = Song("Unlearned Song", "Artist", 2000, False)
    song_collection.add_song(unlearned_song)
    assert song in song_collection.get_learned_songs()
    assert unlearned_song in song_collection.get_unlearned_songs()

    # Test saving songs
    print("Test saving songs:")
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        song_collection.save_songs(temp_file.name)
        temp_file.seek(0)
        saved_data = json.load(temp_file)
        assert saved_data == [{'title': 'My Happiness', 'artist': 'Powderfinger', 'year': 1996, 'learned': True},
                              {'title': 'Unlearned Song', 'artist': 'Artist', 'year': 2000, 'learned': False}]

    # Test loading songs
    print("Test loading songs:")
    new_collection = SongCollection()
    new_collection.load_songs(temp_file.name)
    assert len(new_collection.songs) == 2


run_tests()
