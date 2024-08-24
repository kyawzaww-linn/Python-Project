""" Tests for Song class. """
from song import Song


def run_tests():
    """ Test Song class. """

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    print("Test initial-value song:")
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    assert initial_song.artist == "Powderfinger"
    assert initial_song.title == "My Happiness"
    assert initial_song.year == 1996
    assert initial_song.is_learned

    # Test __str__ method
    print("Test __str__ method:")
    test_song = Song("Title", "Artist", 2000)
    assert str(test_song) == "Title by Artist (2000) - Not Learned"
    test_song.is_learned = True
    assert str(test_song) == "Title by Artist (2000) - Learned"

    # Test mark_learned method
    print("Test mark_learned method:")
    test_song = Song("Title", "Artist", 2000)
    test_song.mark_learned()
    assert test_song.is_learned

    # Test mark_unlearned method
    print("Test mark_unlearned method:")
    test_song = Song("Title", "Artist", 2000, True)
    test_song.mark_unlearned()
    assert not test_song.is_learned


run_tests()
